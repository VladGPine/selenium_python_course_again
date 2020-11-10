import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')


@pytest.fixture(scope='function')
def browser(request):

    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')

        # for linux
        # chrome_options = Options()
        # chrome_options.add_argument("no-sandbox")
        # chrome_options.add_argument("--disable-extensions")
        # browser = webdriver.Chrome('../environments/selenium_env/bin/chromedriver', options=chrome_options)

        # for macOS and windows
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')

        # for macOS and windows
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print('\nquit browser..')
    browser.quit()
