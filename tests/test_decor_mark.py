import pytest


@pytest.mark.smoke
def test_decor_1(browser):
    assert True

@pytest.mark.regress
def test_decor_2(browser):
    assert True

@pytest.mark.regress
def test_decor_3(browser):
    assert True

@pytest.mark.regress
def test_decor_4(browser):
    assert True