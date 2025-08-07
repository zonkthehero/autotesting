from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser..")
    browser.quit()

class TestGuest:
    def test_guest_should_see_login_link_pass(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_login_link_fail(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#magic_link")
