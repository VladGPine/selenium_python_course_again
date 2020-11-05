from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

page = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(page)

    treasure = browser.find_element_by_xpath('//img[@id="treasure"]')
    treasure_value = treasure.get_attribute('valuex')

    answer_input = browser.find_element_by_xpath('//input[@id="answer"]')
    answer_input.send_keys(calc(treasure_value))

    robot_checkbox = browser.find_element_by_id('robotCheckbox')
    robot_checkbox.click()

    robot_radio_button = browser.find_element_by_id('robotsRule')
    robot_radio_button.click()

    submit_button = browser.find_element_by_css_selector('button[type="submit"]')
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()



