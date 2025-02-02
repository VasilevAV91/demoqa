from pages.form_page import FormPage
from selenium.webdriver.common.keys import Keys
import time

def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    form_page.hobbies.click_force()
    form_page.current_address.send_keys('text')
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()


#Задача 10_3 Заполнение полей State, City
def test_check_state_city(browser):
    form_page = FormPage(browser)

    form_page.visit()
    form_page.btn_state.scroll_to_element()
    form_page.btn_state.click()
    time.sleep(5)
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(5)

    form_page.btn_city.scroll_to_element()
    form_page.btn_city.click()
    time.sleep(5)
    form_page.inp_city.send_keys(Keys.ENTER)
    time.sleep(5)





