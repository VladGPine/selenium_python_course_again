from selenium import webdriver
import time

link = "aa"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@name="last_name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[contains(@class, "city")]')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_xpath('//input[@id="country"]')
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("//button[contains(text(), 'Submit')]")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

