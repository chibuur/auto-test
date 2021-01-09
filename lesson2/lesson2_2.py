import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def sum(x,y):
    return str(x+y)


try:
    link="http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #код
    img = browser.find_element_by_css_selector('#num1')
    x = img.text
    x = int(x)
    y_element = browser.find_element_by_css_selector('#num2')
    y = y_element.text
    y = int(y)
    otv = sum(x,y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(otv)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
