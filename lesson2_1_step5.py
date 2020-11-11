import math
from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

page = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Firefox()
    browser.get(page)

    x = browser.find_element_by_id('input_value')
    x = int(x.text)
    y = calc(x)

    answer_input = browser.find_element_by_xpath('//input[@id="answer"]')
    answer_input.send_keys(y)

    robot_checkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    robot_checkbox.click()

    robot_radiobutton = browser.find_element_by_css_selector('[for="robotsRule"]')
    robot_radiobutton.click()

    submit_button = browser.find_element_by_css_selector('button[type="submit"]')
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
