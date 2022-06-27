from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    test_link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(test_link)

    first_name_field = browser.find_element(By.NAME, "firstname")
    first_name_field.send_keys("Татьяна")

    last_name_field = browser.find_element(By.NAME, "lastname")
    last_name_field.send_keys("Татьянова")

    email_field = browser.find_element(By.NAME, "email")
    email_field.send_keys("tanya.tanya@tanya.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    time.sleep(10)

finally:
    time.sleep(10)
    browser.quit()
