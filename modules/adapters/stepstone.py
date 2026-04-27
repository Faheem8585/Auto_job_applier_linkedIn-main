import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class StepstoneAdapter:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username, password):
        print("[Stepstone] Attempting to login...")
        self.driver.get("https://www.stepstone.de/login")
        time.sleep(3)
        
        try:
            # Simple skeleton for stepstone login
            self._fill_field("email", username)
            self._fill_field("password", password)
            self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            time.sleep(5)
            print("[Stepstone] Login complete.")
            return True
        except Exception as e:
            print(f"[Stepstone] Login failed: {e}")
            return False

    def search_and_apply(self, job_keyword, location):
        print(f"[Stepstone] Searching for '{job_keyword}' in '{location}'")
        search_url = f"https://www.stepstone.de/jobs/{job_keyword.replace(' ', '-')}/in-{location.replace(' ', '-')}"
        self.driver.get(search_url)
        time.sleep(5)
        
        # Skeleton loop
        print("[Stepstone] Gathering job cards...")
        # job_cards = self.driver.find_elements(By.CSS_SELECTOR, "article.res-1vw0nnt")
        # for card in job_cards:
        #    card.click()
        #    time.sleep(2)
        #    apply_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Bewerben')]")
        #    apply_button.click()
        return True
        
    def _fill_field(self, field_id: str, value: str):
        try:
            element = self.driver.find_element(By.ID, field_id)
            element.clear()
            element.send_keys(value)
        except Exception:
            pass
