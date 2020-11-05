from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//label[contains(text(), "First name")]/following::input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//label[contains(text(), "Last name")]/following::input')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//label[contains(text(), "Email")]/following::input')
    input3.send_keys("petrov@test.test")

    button = browser.find_element_by_xpath("//button[contains(text(), 'Submit')]")
    button.click()

    time.sleep(5)

    welcome_txt_elem = browser.find_element_by_tag_name('h1')
    welcome_txt = welcome_txt_elem.text

    assert "Congratulations! You have successfully registered!" == welcome_txt

finally:
    time.sleep(10)
    browser.quit()
