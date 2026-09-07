import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    CALL_TAXI_BUTTON = (By.XPATH, '//button[@class="button round"]')
    COMFORT_TARIFF_BUTTON = (By.XPATH, '//div[contains(text(),"Comfort")]')
    PHONE_FIELD_BUTTON = (By.CLASS_NAME, "np-text")
    PHONE_INPUT_FIELD = (By.ID, "phone")
    NEXT_BUTTON_PHONE = (By.XPATH, '//button[text()="Próximo"]')
    SMS_CODE_FIELD = (By.ID, "code")
    CONFIRM_SMS_BUTTON = (By.XPATH, '//button[text()="Confirmar"]')
    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, "pp-text")
    ADD_CARD_BUTTON = (By.XPATH, '//div[contains(text(), "Adicionar cartão")]')
    CARD_NUMBER_INPUT = (By.ID, "number")
    CARD_CVV_INPUT = (By.XPATH, '(//input[@id="code"])')
    LINK_CARD_BUTTON = (By.XPATH, '//button[text()="Adicionar"]')
    CLOSE_PAYMENT_MODAL = (By.XPATH, '//div[contains(@class, "payment-picker")]//button[contains(@class, "close-button")]')
    COMMENT_FIELD = (By.ID, "comment")
    BLANKET_SWITCH = (By.XPATH, '//span[@class="slider round"]')
    BLANKET_CHECKBOX = (By.XPATH, '(//input[@class="switch-input"])')
    ICE_CREAM_PLUS = (By.XPATH, '//div[@class="counter-plus"]')
    ICE_CREAM_COUNTER = (By.XPATH, '(//div[@class="counter-value"])')
    ORDER_TAXI_BUTTON = (By.CLASS_NAME, "smart-button")
    CAR_SEARCH_MODAL = (By.CLASS_NAME, "order-body")

    def __init__(self, driver):
        self.driver = driver

    def set_route(self, from_text, to_text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FROM_INPUT)).send_keys(from_text)
        self.driver.find_element(*self.TO_INPUT).send_keys(to_text)

    def click_call_taxi(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CALL_TAXI_BUTTON)).click()

    def select_comfort_tariff(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.COMFORT_TARIFF_BUTTON)).click()

    def add_phone_number(self, phone_number):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PHONE_FIELD_BUTTON)).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PHONE_INPUT_FIELD)).send_keys(phone_number)
        self.driver.find_element(*self.NEXT_BUTTON_PHONE).click()

    def enter_sms_code(self, sms_code):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SMS_CODE_FIELD)).send_keys(sms_code)
        self.driver.find_element(*self.CONFIRM_SMS_BUTTON).click()

    def add_credit_card(self, card_number, cvv_code):
        payment_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PAYMENT_METHOD_BUTTON))
        self.driver.execute_script("arguments[0].click();", payment_button)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADD_CARD_BUTTON)).click()
        time.sleep(2)
        number_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CARD_NUMBER_INPUT))
        number_field.send_keys(card_number)
        cvv_field = self.driver.find_element(*self.CARD_CVV_INPUT)
        cvv_field.send_keys(cvv_code)
        cvv_field.send_keys(Keys.TAB)
        time.sleep(1)
        link_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LINK_CARD_BUTTON))
        self.driver.execute_script("arguments[0].click();", link_button)
        time.sleep(1)
        close_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CLOSE_PAYMENT_MODAL))
        self.driver.execute_script("arguments[0].click();", close_button)

    def add_driver_comment(self, comment):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.COMMENT_FIELD)).send_keys(comment)

    def select_blanket_and_tissues(self):
        blanket_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.BLANKET_SWITCH))
        self.driver.execute_script("arguments[0].click();", blanket_btn)

    def is_blanket_selected(self):
        return self.driver.find_element(*self.BLANKET_CHECKBOX).is_selected()

    def order_two_ice_creams(self):
        plus_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ICE_CREAM_PLUS))
        self.driver.execute_script("arguments[0].click();", plus_button)
        self.driver.execute_script("arguments[0].click();", plus_button)

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNTER).text

    def click_order_taxi(self):
        order_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ORDER_TAXI_BUTTON))
        self.driver.execute_script("arguments[0].click();", order_button)

    def is_car_search_modal_visible(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CAR_SEARCH_MODAL)).is_displayed()
