from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


page = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.get(page)

    price_element = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = browser.find_element(By.ID, 'book')
    button.click()

    needed_value = browser.find_element(By.ID, 'input_value').text
    input_element = browser.find_element(By.ID, 'answer')
    button_element_to_solve_the_task = browser.find_element(By.ID, 'solve')
    input_element.send_keys(calc(needed_value))
    button_element_to_solve_the_task.click()
    
finally:
    time.sleep(5)
    browser.quit()
