from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math

try: 
    browser = webdriver.Chrome()

    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )

    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    equation = math.log(abs(12*math.sin(x)))

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(equation)

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
