import time

import pytest
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.demoqa import DemoQa
from pages.browser_tab import BrowserTab


@pytest.mark.parametrize('pages', [Accordion, Alerts, DemoQa,BrowserTab])
def test_check_meta_teg(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.meta_teg.exist()
    assert page.meta_teg.get_dom_attribute('name') == 'viewport'
    assert page.meta_teg.get_dom_attribute('content') == 'width=device-width,initial-scale=1'