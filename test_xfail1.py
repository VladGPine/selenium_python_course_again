from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")

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


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('#login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.xfail
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('button.favorite')
