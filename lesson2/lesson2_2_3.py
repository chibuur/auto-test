import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
def sum(x,y):
    return str(x+y)

try:
    link="http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

#value
    img = browser.find_element_by_css_selector('#num1')
    x = img.text
    x = int(x)
    y_element = browser.find_element_by_css_selector('#num2')
    y = int(y)
    y = y_element.text
    otv = sum(x,y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value("otv")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
