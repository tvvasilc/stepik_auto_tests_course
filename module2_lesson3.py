from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


test_link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(test_link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(3)
    confirm = browser.switch_to.alert
    time.sleep(3)
    confirm.accept()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    text_field = browser.find_element(By.ID, "answer")
    text_field.send_keys(y)
    button_2 = browser.find_element(By.TAG_NAME, "button")
    button_2.click()

finally:
    time.sleep(10)
    browser.quit()
