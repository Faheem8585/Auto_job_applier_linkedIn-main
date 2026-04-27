import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class LeverAdapter:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def apply(self, url: str, personals: dict):
        print(f"[Lever] Navigating to {url}")
        # Lever usually appends /apply to the job URL for the form
        if not url.endswith("/apply"):
            url += "/apply"
        
        self.driver.get(url)
        time.sleep(3)
        
        try:
            print("[Lever] Attempting to fill basic details...")
            
            # Lever name is usually one field
            full_name = f"{personals.get('first_name', '')} {personals.get('last_name', '')}"
            self._fill_name("name", full_name)
            self._fill_name("email", personals.get("email", ""))
            self._fill_name("phone", personals.get("phone", ""))
            self._fill_name("org", personals.get("recent_employer", ""))
            self._fill_name("urls[LinkedIn]", personals.get("linkedin", ""))
            self._fill_name("urls[Portfolio]", personals.get("website", ""))
            
            print("[Lever] Basic parsing handled.")
            return True
        except Exception as e:
            print(f"[Lever] Failed during apply sequence: {e}")
            return False

    def _fill_name(self, name_attr: str, value: str):
        try:
            element = self.driver.find_element(By.NAME, name_attr)
            element.clear()
            element.send_keys(value)
        except Exception:
            pass
