import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium import webdriver

LINKS = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"]

my_login = 'test_login'
my_pass = 'test_pass'

@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser..")
    browser.quit()

@pytest.mark.parametrize('link', LINKS)
class TestGetText:
    def test_check_links(self, browser, link):
        answer = str(math.log(int(time.time())))
        browser.get(link)

        login_btn = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, 
                '.navbar__auth_login'
            ))
        )
        login_btn.click()

        email_field = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, '#id_login_email'))
        )
        email_field.clear()
        email_field.send_keys(my_login)

        pass_field = browser.find_element(By.CSS_SELECTOR, '#id_login_password')
        pass_field.clear()
        pass_field.send_keys(my_pass)

        time.sleep(2)
        submit_login_btn = browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader')
        submit_login_btn.click()

        WebDriverWait(browser, 5).until_not(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, '.light-tabs.ember-view'
            ))
        )

        try:
            try_again_btn = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, '.again-btn.white'
            ))
        )
            try_again_btn.click()
        except TimeoutException:
            print('Задание решается впервые')

        text_area = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, 
                'textarea.ember-text-area.ember-view.textarea.string-quiz__textarea'
            ))
        )
        text_area.send_keys(answer)

        submit_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission'))
            )
        submit_button.click()

        feedback = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, '.smart-hints__hint'))
        )
        assert 'correct' in feedback.text.lower(), f'Unexpected feedback: {feedback.text}'
