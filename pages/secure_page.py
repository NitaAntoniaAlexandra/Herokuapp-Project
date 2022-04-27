from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class Secure_page(BasePage):

    def assert_secure_page(self):
        actual = self.driver.current_url
        expected = 'https://the-internet.herokuapp.com/secure'
        self.assertEqual(actual, expected, 'URL is incorrect')
