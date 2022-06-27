from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


test_link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(test_link)

    picture = browser.find_element(By.ID, "treasure")
    value_x = picture.get_attribute("valuex")
    value_y = calc(value_x)

    text_field = browser.find_element(By.ID, "answer")
    text_field.send_keys(value_y)

    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()

    radiobutton1 = browser.find_element(By.ID, "robotsRule")
    radiobutton1.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
