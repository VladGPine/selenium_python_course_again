from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

page = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(page)
    start_alert_button = browser.find_element_by_css_selector('button[type="submit"]')
    start_alert_button.click()

    window2 = browser.window_handles[1]
    browser.switch_to.window(window2)

    value_for_input = browser.find_element_by_id('input_value')
    input_for_result = browser.find_element_by_id('answer')
    input_for_result.send_keys(calc(value_for_input.text))

    submit_button = browser.find_element_by_css_selector('button[type="submit"]')
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()