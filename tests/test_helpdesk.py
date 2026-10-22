import pytest
from selenium.webdriver.common.by import By
from pages.helpdesk import HelpdeskPage

@pytest.fixture
def page(driver, helpdesk_url):
    driver.get(helpdesk_url)
    return HelpdeskPage(driver)

@pytest.mark.parametrize('priority', ['Normal','High'])
def test_create_ticket(page, priority):
    page.create_ticket('VPN connection fails',priority)
    assert page.tickets == [f'VPN connection fails — {priority}']
    assert page.driver.find_element(By.ID,'status').text=='Ticket created.'

@pytest.mark.parametrize('summary', ['', '   '])
def test_reject_blank_summary(page, summary):
    page.create_ticket(summary)
    assert page.tickets==[]

def test_filter_and_clear(page):
    page.create_ticket('VPN unavailable')
    page.create_ticket('Printer offline')
    page.filter('vpn')
    assert page.tickets==['VPN unavailable — Normal']
    page.filter('no-match')
    assert page.tickets==[]
    page.filter('')
    assert len(page.tickets)==2
    page.driver.find_element(By.ID,'reset').click()
    assert page.tickets==[]

def test_html_is_text(page):
    text='<img src=x onerror="window.injected=true">'
    page.create_ticket(text)
    assert page.tickets==[text+' — Normal']
    assert page.driver.execute_script('return window.injected') is None
    assert page.driver.find_elements(By.CSS_SELECTOR,'#tickets img')==[]

def test_summary_length_constraint(page):
    page.create_ticket('a'*130)
    assert page.tickets==['a'*120+' — Normal']
