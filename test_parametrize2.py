import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import math


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test..')

    # for linux
    chrome_options = Options()
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("--disable-extensions")
    browser = webdriver.Chrome('../environments/selenium_env/bin/chromedriver', options=chrome_options)
    browser.implicitly_wait(5)
    # for macOS and windows
    # self.browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()


@pytest.mark.parametrize('links', (
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
))
def test_correct_answer(browser, links):
    browser.get(links)
    input_for_answer = browser.find_element_by_css_selector('textarea')
    input_for_answer.send_keys(str(math.log(int(time.time()))))
    submit_button = browser.find_element_by_css_selector('button.submit-submission')
    submit_button.click()
    actual_answer = browser.find_element_by_css_selector('.smart-hints__hint').text
    expected_answer = 'Correct!'
    assert actual_answer == expected_answer, f'{actual_answer} not equal {expected_answer}'
