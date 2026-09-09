import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_complete_taxi_order(self):
        self.driver.get("https://cnt-61aad21e-08e1-452b-8429-98acd5949c86.containerhub.tripleten-services.com?lng=pt")
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.set_route("East 2nd Street, 601", "1300 1st St")
        routes_page.click_call_taxi()
        routes_page.select_comfort_tariff()

        phone_number = "+11234567890"
        routes_page.add_phone_number(phone_number)
        sms_code = helpers.retrieve_phone_code(self.driver)
        routes_page.enter_sms_code(sms_code)
        time.sleep(2)

        routes_page.add_credit_card("1234567890123456", "12")
        routes_page.add_driver_comment("Trazer troco para 50")
        routes_page.select_blanket_and_tissues()
        assert routes_page.is_blanket_selected() is True

        routes_page.order_ice_creams(2)
        assert routes_page.get_ice_cream_count() == 2

        routes_page.click_order_taxi()
        assert routes_page.is_car_search_modal_visible() is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

