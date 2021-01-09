import math
import time
from selenium import webdriver
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link="http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #код
    
    button2 = browser.find_element_by_css_selector("button.btn")
    button2.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    poisk = browser.find_element_by_css_selector('#input_value')
    x_element = poisk.text
    x2 = calc(x_element)
    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(x2)
    button2 = browser.find_element_by_css_selector("button.btn")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()
