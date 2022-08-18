import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage(unittest.TestCase):
    USER = (By.XPATH, '//input[@id="username"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')
    SUBMIT = (By.XPATH, '//button[@class="radius"]')
    LOGIN_ERROR = (By.XPATH, '//div[contains(text(),"logged")]')
    LOGOUT = (By.XPATH, '//a[@class="button secondary radius"]')
    LOGOUT_ERR = (By.XPATH, '//div[@class="flash success"]')
    USER_PASS_ERR = (By.XPATH, '//div[@class="flash error"]')

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def login(self):
        self.driver.find_element(*self.USER).send_keys("tomsmith")
        self.driver.find_element(*self.PASSWORD).send_keys("SuperSecretPassword!")
        self.driver.find_element(*self.SUBMIT).click()

    def test_enter_wrong_user_password(self):
        self.driver.find_element(*self.USER).send_keys("xxxx")
        self.driver.find_element(*self.PASSWORD).send_keys("xxxx")
        self.driver.find_element(*self.SUBMIT).click()
        err_msg = self.driver.find_element(*self.USER_PASS_ERR).text
        self.assertIn(err_msg, 'Your username is invalid!\n×', 'Incorrect username and password error msg')

    def test_login_empty_fields(self):
        self.driver.find_element(*self.SUBMIT).click()
        err_msg = self.driver.find_element(*self.USER_PASS_ERR).text
        self.assertIn(err_msg, 'Your username is invalid!\n×', 'Incorrect username and password error msg')

    def test_login_correct_credentials(self):
        self.login()
        expected = self.driver.find_element(*self.LOGIN_ERROR).text
        actual = 'You logged into a secure area!\n×'
        self.assertEqual(expected, actual, 'Not the correct error message')

    def test_logout_err_msg(self):
        self.login()
        self.driver.find_element(*self.LOGOUT).click()
        err_msg = self.driver.find_element(*self.LOGOUT_ERR).text
        self.assertIn(err_msg, 'You logged out of the secure area!\n×', 'Not the correct error message')
