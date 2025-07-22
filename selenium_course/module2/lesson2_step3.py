from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time 
import math

#link = "https://suninjuly.github.io/selects1.html"
link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    y_element = browser.find_element(By.ID, "num2")
    x = x_element.text
    y = y_element.text

    sum = int(x)+int(y)

    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(str(sum))

    browser.find_element(By.CLASS_NAME, "btn.btn-default").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла