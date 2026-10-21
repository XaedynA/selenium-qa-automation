import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    if os.getenv('HEADLESS', '0') == '1':
        options.add_argument('--headless=new')
    options.add_argument('--window-size=1280,900')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(options=options)
    browser.set_page_load_timeout(20)
    yield browser
    browser.quit()
