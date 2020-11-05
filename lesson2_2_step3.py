from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

page = 'http://suninjuly.github.io/selects2.html'
try:
    browser = webdriver.Chrome()
    browser.get(page)

    num_1 = browser.find_element_by_id('num1')
    num_2 = browser.find_element_by_id('num2')
    sum_of_numbers = int(num_1.text) + int(num_2.text)

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(sum_of_numbers))

    submit_button = browser.find_element_by_css_selector('button[type="submit"]')
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
