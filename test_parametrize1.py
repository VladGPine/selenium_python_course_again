import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test..')

    # for linux
    chrome_options = Options()
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("--disable-extensions")
    browser = webdriver.Chrome('../environments/selenium_env/bin/chromedriver', options=chrome_options)

    # for macOS and windows
    # self.browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()


@pytest.mark.parametrize('language', ['ru', 'en-gb'])
def test_guest_should_see_login_link(browser, language):
    link = f'http://selenium1py.pythonanywhere.com/{language}'
    browser.get(link)
    browser.find_element_by_css_selector('#login_link')
