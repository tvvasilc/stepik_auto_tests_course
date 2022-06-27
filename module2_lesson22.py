from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


test_link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(test_link)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    text_field = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", text_field)
    text_field.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobutton1 = browser.find_element(By.ID, "robotsRule")
    radiobutton1.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
#
finally:
    time.sleep(10)
    browser.quit()
