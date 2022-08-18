import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DropDown(unittest.TestCase):
    DROPDOWN_PG = (By.XPATH, '//a[contains(text(),"Dropdown")]')
    DROPDOWN_INPUT = (By.XPATH, '//select[@id="dropdown"]')
    OPTION_ONE = (By.XPATH, '(//select[@id="dropdown"]//parent::option)[2]')
    OPTION_TWO = (By.XPATH, '(//select[@id="dropdown"]//parent::option)[3]')

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://the-internet.herokuapp.com")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.find_element(*self.DROPDOWN_PG).click()

    def tearDown(self):
        self.driver.quit()

    def verifying_option_one(self):
        expected = self.driver.find_element(*self.OPTION_ONE).text
        self.assertIn('Option 1', expected, 'Action not performed')

    def test_drop_choose_option1(self):
        self.driver.find_element(*self.DROPDOWN_INPUT).click()
        self.driver.find_element(*self.OPTION_ONE).click()
        self.verifying_option_one()

    def test_drop_clickable(self):
        self.driver.find_element(*self.DROPDOWN_INPUT).click()
        self.driver.find_element(*self.DROPDOWN_INPUT).click()
        expected = self.driver.find_element(By.XPATH, '(//select[@id="dropdown"]//parent::option)[1]').text
        actual = 'Please select an option'
        self.assertEqual(expected, actual, 'Action not performed')

    def test_drop_multiple_times(self):
        self.driver.find_element(*self.DROPDOWN_INPUT).click()
        self.driver.find_element(*self.OPTION_ONE).click()
        self.driver.find_element(*self.OPTION_ONE).click()
        self.driver.find_element(*self.OPTION_TWO).click()
        self.driver.find_element(*self.OPTION_ONE).click()
        self.verifying_option_one()
