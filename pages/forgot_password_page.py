from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class Forgot_password_page(BasePage):
    EMAIL = (By.XPATH, '//input[@id="email"]')
    RETRIEVE_PASSWORD_BTN = (By.XPATH, '//i[contains(text(),"pass")] ')
    ERROR_MESSAGE = (By.XPATH, '//h1[text()="Internal Server Error"]')

    def navigate_to_forgot_password_page(self):
        self.driver.get('https://the-internet.herokuapp.com/forgot_password')
        sleep(3)

    def insert_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def click_retrieve_password_btn(self):
        self.driver.find_element(*self.RETRIEVE_PASSWORD_BTN).click()

    def display_error_message(self):
        error = self.driver.find_element(*self.ERROR_MESSAGE)
        self.assertTrue(error.is_displayed(), 'Error message is not displayed')
