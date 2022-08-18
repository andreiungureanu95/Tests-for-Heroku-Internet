import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class AddRemove(unittest.TestCase):
    ADD_REMOVE = (By.LINK_TEXT, "Add/Remove Elements")
    ADD = (By.CSS_SELECTOR, "#content > div > button")
    DELETE = (By.CLASS_NAME, "added-manually")
    CONTAINER = (By.XPATH, '/html/body/div[2]')

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_remove_elements(self):
        self.driver.find_element(*self.ADD_REMOVE).click()
        self.driver.find_element(*self.ADD).click()
        self.driver.find_element(*self.ADD).click()
        self.driver.find_element(*self.ADD).click()
        self.driver.find_element(*self.DELETE).click()
        self.driver.find_element(*self.DELETE).click()
        self.driver.find_element(*self.DELETE).click()
        self.assertIsNotNone(self.DELETE, 'Test Failed!')
        print('', 'Test Passed!')

