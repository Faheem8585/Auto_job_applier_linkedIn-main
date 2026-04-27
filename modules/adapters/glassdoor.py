import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class GlassdoorAdapter:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username, password):
        print("[Glassdoor] Attempting to login...")
        self.driver.get("https://www.glassdoor.com/profile/login")
        time.sleep(3)
        
        try:
            # Handle possible bot challenge or login form
            self.driver.find_element(By.ID, "inlineUserEmail").send_keys(username)
            self.driver.find_element(By.NAME, "submit").click()
            time.sleep(2)
            self.driver.find_element(By.ID, "inlineUserPassword").send_keys(password)
            self.driver.find_element(By.NAME, "submit").click()
            time.sleep(5)
            print("[Glassdoor] Login complete.")
            return True
        except Exception as e:
            print(f"[Glassdoor] Login failed (Likely CAPTCHA blocked): {e}")
            return False

    def search_and_apply(self, job_keyword, location):
        print(f"[Glassdoor] Searching for '{job_keyword}' in '{location}'")
        search_url = f"https://www.glassdoor.com/Job/jobs.htm?sc.keyword={job_keyword}&locT=C&locId=1&locKeyword={location}"
        self.driver.get(search_url)
        time.sleep(5)
        
        print("[Glassdoor] Navigating 'Easy Apply' listings...")
        # job_cards = self.driver.find_elements(By.CSS_SELECTOR, "li[data-test='jobListing']")
        # for card in job_cards:
        #    card.click()
        #    time.sleep(2)
        #    # Look for Easy Apply button
        return True
