import hashlib
import os
from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption('--external', action='store_true', help='Also test example.com; requires internet')


def pytest_collection_modifyitems(config, items):
    if not config.getoption('--external'):
        for item in items:
            if 'external' in item.keywords:
                item.add_marker(pytest.mark.skip(reason='Use --external for live-site smoke tests'))


@pytest.fixture
def driver():
    options = Options()
    if os.getenv('HEADLESS', '1') == '1':
        options.add_argument('--headless=new')
    options.add_argument('--window-size=1280,900')
    if os.getenv('CHROME_NO_SANDBOX') == '1':
        options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    if os.getenv('CHROME_BINARY'):
        options.binary_location = os.environ['CHROME_BINARY']
    service = Service(executable_path=os.environ['CHROMEDRIVER']) if os.getenv('CHROMEDRIVER') else Service()
    browser = webdriver.Chrome(options=options, service=service)
    try:
        browser.set_page_load_timeout(20)
        yield browser
    finally:
        browser.quit()


@pytest.fixture
def helpdesk_url():
    return (Path(__file__).resolve().parents[1]/'fixtures/helpdesk.html').as_uri()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed and 'driver' in item.funcargs:
        folder = Path('artifacts'); folder.mkdir(exist_ok=True)
        name = hashlib.sha256(item.nodeid.encode()).hexdigest()[:16]
        try:
            item.funcargs['driver'].save_screenshot(str(folder/f'{name}.png'))
        except Exception:
            pass  # Artifact failure must not hide the original test failure.
