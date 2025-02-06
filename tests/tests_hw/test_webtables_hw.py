import time
from pages.webtables import WebTables


def test_webtables(browser):
    webtables = WebTables(browser)
    webtables.visit()

    # считаем количество пустых строк
    empty_row_before_add = len(webtables.empty_row.find_elements())

    webtables.btn_add.click()
    time.sleep(5)
    assert webtables.modal.exist()
    webtables.btn_submit.click()
    assert webtables.form.get_dom_attribute('class') == 'was-validated'
    assert webtables.modal.exist()
    time.sleep(5)
    webtables.first_name.send_keys('Ivan')
    webtables.last_name.send_keys('Petrov')
    webtables.email.send_keys('aaa@bbbb.com')
    webtables.age.send_keys('25')
    webtables.salary.send_keys('100000')
    webtables.departament.send_keys('DIT')
    time.sleep(5)
    webtables.btn_submit.click()
    assert not webtables.modal.exist()

    # считаем количество пустых строк после ввода
    empty_row_after_add = len(webtables.empty_row.find_elements())

    # сравниваем значения до и после
    assert not empty_row_before_add == empty_row_after_add

    webtables.btn_edit.click()
    webtables.first_name.clear()
    webtables.first_name.send_keys('Oleg')
    webtables.btn_submit.click()
    time.sleep(5)

    assert webtables.first_name_line_1.get_text() == 'Oleg'

    webtables.btn_delete_row.click()
    time.sleep(5)
    empty_row_after_delete = len(webtables.empty_row.find_elements())
    assert not empty_row_after_delete == empty_row_after_add



def test_webtables_2(browser):
    webtables = WebTables(browser)
    webtables.visit()

    webtables.rows_per_page.click()
    time.sleep(2)

    assert not webtables.btn_next.click()
    assert webtables.btn_next.get_dom_attribute('disabled')
    assert not webtables.btn_previous.click()
    assert webtables.btn_previous.get_dom_attribute('disabled')

    # создаем словарь с новвыми работниками
    dct = {'worker_4':['Petr', 'Petrov', 'aaa@bbb.com', '25', '10000', 'AU'],
           'worker_5':['Igor', 'Sidorov', 'bbb@ccc.com', '35', '20000', 'UB'],
           'worker_6':['Artem', 'Golubev', 'vvv@ttt.com', '45', '30000', 'UKO']}

    # перебираем ключи словаря и заполняем поля значениями
    for i in dct.keys():
        webtables.btn_add.click()
        webtables.first_name.send_keys(dct[i][0])
        webtables.last_name.send_keys(dct[i][1])
        webtables.email.send_keys(dct[i][2])
        webtables.age.send_keys(dct[i][3])
        webtables.salary.send_keys(dct[i][4])
        webtables.departament.send_keys(dct[i][5])
        webtables.btn_submit.click()
        time.sleep(2)

    # проверяем, что стало 2 страницы
    assert webtables.total_pages.get_text() == '2'

    # проверяем, что кнопка активна
    assert not webtables.btn_next.get_dom_attribute('disabled')
    webtables.btn_next.click()

    # проверяем переход на страницу 2
    assert webtables.page_number.get_dom_attribute('value') == '2'

    # проверяем, что кнопка активна
    assert not webtables.btn_previous.get_dom_attribute('disabled')
    webtables.btn_previous.click()

    # проверяем переход на страницу 1
    assert webtables.page_number.get_dom_attribute('value') == '1'

