import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class BrokenImage(unittest.TestCase):
    IMG = (By.XPATH, '(//div[@class="example"]//parent::h3//following-sibling::img)[1]')

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://the-internet.herokuapp.com/broken_images")
        self.driver.maximize_window()

    def test_broken_img_displayed(self):
        displayed_img = self.driver.find_element(*self.IMG).is_displayed()
        self.assertTrue(displayed_img is True, "Test Failed!")

    def tearDown(self):
        self.driver.quit()
