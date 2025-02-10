import time

from pages.progress_bar import ProgressBar


def test_progress(browser):
    progress = ProgressBar(browser)

    progress.visit()
    time.sleep(2)

    progress.start_stop_btn.click()
    while True:
        if progress.progress_bar.get_dom_attribute('aria-valuenow') == '51':
            progress.start_stop_btn.click()
            break

    time.sleep(10)
    assert progress.progress_bar.get_dom_attribute('aria-valuenow') == '51'
