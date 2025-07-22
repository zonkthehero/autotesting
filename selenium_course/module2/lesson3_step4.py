from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "https://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    blue_button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    blue_button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    equation = math.log(abs(12*math.sin(x)))

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(equation)

    submit_button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()
