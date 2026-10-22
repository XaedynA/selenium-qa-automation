from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class HelpdeskPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def create_ticket(self, summary, priority='Normal'):
        field = self.wait.until(EC.visibility_of_element_located((By.ID, 'summary')))
        field.clear()
        field.send_keys(summary)
        Select(self.driver.find_element(By.ID, 'priority')).select_by_visible_text(priority)
        self.driver.find_element(By.ID, 'create').click()

    @property
    def tickets(self):
        return [e.text for e in self.driver.find_elements(By.CSS_SELECTOR, '#tickets li')]

    def filter(self, query):
        field = self.driver.find_element(By.ID, 'filter')
        field.clear()
        field.send_keys(query)
