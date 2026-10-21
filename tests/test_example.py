
from urllib.parse import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://example.com/"


def test_page_title(driver):
    driver.get(BASE_URL)
    assert "Example Domain" in driver.title


def test_page_content_is_visible(driver):
    driver.get(BASE_URL)

    body = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "body"))
    )

    assert "example" in body.text.lower()


def test_more_information_link(driver):
    driver.get(BASE_URL)

    link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[href*="iana.org"]')
        )
    )

    href = link.get_attribute("href")
    parsed_url = urlparse(href)

    assert parsed_url.scheme == "https"
    assert parsed_url.hostname in ("iana.org", "www.iana.org")
