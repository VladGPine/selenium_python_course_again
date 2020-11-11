import time

page = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_button_present_on_the_page(browser):
    browser.get(page)
    time.sleep(5)
    buttons = browser.find_elements_by_xpath('//button[contains(@class, "btn-add-to-basket")]')
    assert len(buttons) > 0, 'No any basket buttons on the page'
