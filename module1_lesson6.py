from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    target_link_1 = "http://suninjuly.github.io/registration1.html"
    # target_link_2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(target_link_1)
    # после успешного прохождения теста для target_link_1:
    # -в методе get() заменить аргумент target_link_1 на target_link_2;
    # -раскомментировать строку кода с инициализацией target_link_2;
    # -закомментировать строку кода с инициализацией target_link_1.

    first_name_field = browser.find_element(By.CSS_SELECTOR, "input.first:required")
    first_name_field.send_keys("Татьяна")

    last_name_field = browser.find_element(By.CSS_SELECTOR, "input.second:required")
    last_name_field.send_keys("Татьянова")

    email_field = browser.find_element(By.CSS_SELECTOR, "input.third:required")
    email_field.send_keys("tanya.tanya@tanya.ru")

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
