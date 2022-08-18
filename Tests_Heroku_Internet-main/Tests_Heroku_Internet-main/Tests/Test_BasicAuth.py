import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class BasicAuth(unittest.TestCase):
    AUTH_BUTTON = (By.CSS_SELECTOR, "#content > ul > li:nth-child(3)")
    MESSAGE = (By.CSS_SELECTOR, "#content > div > p")

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.find_element(*self.AUTH_BUTTON).click()

    def test_basic_auth(self):
        user = 'admin'
        password = 'admin'
        self.driver.get("https://" + user + ":" + password + "@the-internet.herokuapp.com/basic_auth")
        message = self.driver.find_element(*self.MESSAGE).text
        self.assertTrue('proper credentials' in message)
        print('', message)
        self.driver.back()
        self.driver.back()

    def tearDown(self):
        self.driver.quit()
