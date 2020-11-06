from selenium import webdriver
import math
import time

page = 'http://SunInJuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(page)
    x = browser.find_element_by_id('input_value')
    answer_input = browser.find_element_by_id('answer')
    answer_input.send_keys(calc(x.text))
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    robot_radio_button = browser.find_element_by_id('robotsRule')
    submit_button = browser.find_element_by_css_selector('button[type="submit"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', submit_button)
    robot_radio_button.click()
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
