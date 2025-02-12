import pytest

from  pages.alerts import Alerts
import time

@pytest.mark.skip
def test_allert(browser):
    allert_page = Alerts(browser)

    allert_page.visit()
    assert not allert_page.alert()

    allert_page.alert_btn.click()
    time.sleep(2)
    assert allert_page.alert()

@pytest.mark.skip
def test_allert_text(browser):
    allert_page = Alerts(browser)

    allert_page.visit()
    allert_page.alert_btn.click()
    time.sleep(2)
    assert allert_page.alert().text == 'You clicked a button'

    allert_page.alert().accept()
    assert not allert_page.alert()

@pytest.mark.skip
def test_confirm(browser):
    allert_page = Alerts(browser)

    allert_page.visit()
    allert_page.confirm_btn.click()
    time.sleep(2)
    allert_page.alert().dismiss()
    assert allert_page.confirm_result.get_text() == 'You selected Cancel'


def test_prompt(browser):
    allert_page = Alerts(browser)
    name = 'Anton'
    allert_page.visit()
    allert_page.prompt_btn.click()
    time.sleep(2)
    allert_page.alert().send_keys(name)
    allert_page.alert().accept()
    assert allert_page.prompt_result.get_text() == f'You entered {name}'
