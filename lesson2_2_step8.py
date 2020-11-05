from selenium import webdriver
import time
import os

page = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(page)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    name_input = browser.find_element_by_css_selector('input[name="firstname"]')
    last_name_input = browser.find_element_by_css_selector('input[name="lastname"]')
    email_input = browser.find_element_by_css_selector('input[name="email"]')
    upload_button = browser.find_element_by_id('file')
    submit_button = browser.find_element_by_css_selector('button[type="submit"]')

    name_input.send_keys('name')
    last_name_input.send_keys('last_name')
    email_input.send_keys('email.test@email.com')
    upload_button.send_keys(file_path)
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
