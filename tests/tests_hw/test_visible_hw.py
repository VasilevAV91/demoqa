from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    accordian_page = Accordion(browser)

    accordian_page.visit()
    assert accordian_page.text_accordian.visible()
    accordian_page.btn_lorem_ipsum.click()
    time.sleep(2)
    assert not accordian_page.text_accordian.visible()

def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()

    assert not accordion_page.text_come_from_1.visible()
    assert not accordion_page.text_come_from_2.visible()
    assert not accordion_page.text_use_it.visible()