from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class Home_page(BasePage):
    FORM_AUTHENTICATION = (By.XPATH, '//a[@href="/login"]')
    CHECKBOXES = (By.XPATH, '//a[@href="/checkboxes"]')
    FORGOT_PASSWORD = (By.XPATH, '//a[@href="/forgot_password"]')

    def navigate_to_home_page(self):
        self.driver.get('https://the-internet.herokuapp.com/')
        sleep(3)

    def click_form_auth(self):
        self.driver.find_element(*self.FORM_AUTHENTICATION).click()
        sleep(3)

    def click_forgot_password(self):
        self.driver.find_element(*self.FORGOT_PASSWORD).click()

