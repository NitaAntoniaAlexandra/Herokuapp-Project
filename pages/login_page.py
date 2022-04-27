from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class Login_page(BasePage):
    USERNAME = (By.XPATH, '//input[@id="username"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BTN = (By.XPATH, '//i[contains(text(),"Login")]')

    def navigate_to_login_page(self):
        self.driver.get('https://the-internet.herokuapp.com/login')
        sleep(3)

    def insert_username(self, username):
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def insert_password(self, password):
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*self.LOGIN_BTN).click()
