import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.clickers_and_finders import text_input_by_ID

class GreenhouseAdapter:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def apply(self, url: str, personals: dict):
        print(f"[Greenhouse] Navigating to {url}")
        self.driver.get(url)
        time.sleep(3)
        
        try:
            # Fill out standard Greenhouse application fields
            print("[Greenhouse] Attempting to fill basic details...")
            
            # Name
            self._fill_field("first_name", personals.get("first_name", ""))
            self._fill_field("last_name", personals.get("last_name", ""))
            
            # Contact
            self._fill_field("email", personals.get("email", ""))
            self._fill_field("phone", personals.get("phone", ""))
            
            # Resume/CV upload wrapper (usually an input type=file, but requires un-hiding in some ATS)
            # self.driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(personals.get("resume_path"))
            
            print("[Greenhouse] Basic parsing handled. Complex custom questions require manual AI processing hooks.")
            
            # Submit
            # self.driver.find_element(By.ID, "submit_app").click()
            print("[Greenhouse] Draft application complete.")
            return True
        except Exception as e:
            print(f"[Greenhouse] Failed during apply sequence: {e}")
            return False

    def _fill_field(self, field_id: str, value: str):
        try:
            element = self.driver.find_element(By.ID, field_id)
            element.clear()
            element.send_keys(value)
        except Exception:
            pass
