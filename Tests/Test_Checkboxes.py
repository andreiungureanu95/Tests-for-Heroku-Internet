import unittest
from tkinter import *
from tkinter import ttk

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Checkboxes(unittest.TestCase):
    CHECKBOX_PAGE = (By.XPATH, '//a[contains(text(),"Checkboxes")]')
    CHECKBOX = (By.XPATH, '(//input[@type="checkbox"])[1]')

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.implicitly_wait(6)
        self.driver.find_element(*self.CHECKBOX_PAGE).click()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_click_on_checkboxes(self):
        self.driver.find_element(*self.CHECKBOX).click()
        expected = self.driver.find_element(*self.CHECKBOX).is_selected()
        self.assertTrue = expected, True, 'Checkbox not selected'




