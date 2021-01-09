import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link="http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #код
    
    book = browser.find_element_by_css_selector('#book')
    browser.execute_script("return arguments[0].scrollIntoView(true);", book)
    price = WebDriverWait(browser, 14).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    book.click()
    
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)
    button = browser.find_element_by_css_selector('#solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
