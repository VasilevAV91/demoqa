from pages.text_box import TextBox
import time

def test_text_box_form(browser):
    text_box_page = TextBox(browser)

    full_name = 'Ivan'
    current_address = 'Russia, Saint-Petersburg'

    text_box_page.visit()
    text_box_page.full_name.send_keys(full_name)
    text_box_page.current_address.send_keys(current_address)
    text_box_page.btn_submit.click_force()
    time.sleep(5)

    assert text_box_page.test_name.get_text() == 'Name:' + full_name
    if text_box_page.current_address.get_dom_attribute('class') == 'mb-1':
        assert text_box_page.current_address.get_text() == 'Current Address :' + current_address