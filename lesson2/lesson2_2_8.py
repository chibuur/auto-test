import math
import time
from selenium import webdriver
import os

try:
    link="http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #код
    

    input1 = browser.find_element_by_css_selector('[name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('[name="lastname"]')
    input2.send_keys("Prohorov")
    input3 = browser.find_element_by_css_selector('[name="email"]')
    input3.send_keys("pochta")
    
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'blank.txt')           # добавляем к этому пути имя файла
    element = browser.find_element_by_css_selector("[type='file']")
    element.send_keys(file_path)
    
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
