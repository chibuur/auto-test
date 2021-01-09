import math
import time
from selenium import webdriver
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link="http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #код
    img = browser.find_element_by_css_selector('#treasure')
    x_element = img.get_attribute("valuex")
    #x = x_element
    y = calc(x_element)
    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)
    option1 = browser.find_element_by_css_selector('#robotCheckbox')
    option1.click()
    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
