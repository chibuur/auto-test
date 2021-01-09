import math
import time
from selenium import webdriver
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link="http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #код
    
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    option1 = browser.find_element_by_css_selector('#robotCheckbox')
    option1.click()
    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()
