from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'https://example.com/'

def test_page_title(driver):
    driver.get(BASE_URL)
    assert driver.title == 'Example Domain'

def test_heading_is_visible(driver):
    driver.get(BASE_URL)
    heading = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'h1'))
    )
    assert heading.text == 'Example Domain'

def test_more_information_link(driver):
    driver.get(BASE_URL)
    link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href]'))
    )
    assert link.get_attribute('href').startswith('https://www.iana.org/')
