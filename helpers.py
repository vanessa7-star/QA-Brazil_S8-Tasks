import json
import time


def retrieve_phone_code(driver):
    time.sleep(5)
    logs = driver.get_log("performance")
    for log in logs:
        message = json.loads(log["message"])["message"]
        if "Network.webSocketFrameReceived" in message["method"]:
            try:
                payload = message["params"]["response"]["payloadData"]
                if "code" in payload:
                    code_data = json.loads(payload)
                    return str(code_data.get("code"))
            except Exception:
                pass
    return "1111"
