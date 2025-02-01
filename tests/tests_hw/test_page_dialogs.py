import time

from pages.demoqa import DemoQa
from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)

    modal_dialogs.visit()
    assert modal_dialogs.btns_second_menu.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser)
    demo_qa_page = DemoQa(browser)

    modal_dialogs.visit()
    browser.refresh()

    modal_dialogs.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    time.sleep(15)
    browser.forward()

    assert demo_qa_page.equal_url()
    assert browser.title == 'DEMOQA'

    browser.set_window_size(1000, 1000)