from pages.slider import Slider
from selenium.webdriver.common.keys import Keys


def test_slider(browser):
    slider = Slider(browser)

    slider.visit()
    assert slider.slider.exist()
    assert slider.slider_value.exist()

    while not slider.slider_value.get_dom_attribute('value') == '50':
        slider.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider.slider_value.get_dom_attribute('value') == '50'

