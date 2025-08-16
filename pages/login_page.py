from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")

    def load(self):
        self.driver.get(self.URL)

    def login(self, user, pwd):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(user)
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(pwd)
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()
