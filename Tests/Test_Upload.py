import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Upload(unittest.TestCase):
    UPLOAD_PAGE = (By.XPATH, '//a[contains(text(),"File Upload")]')
    CHOOSE_FILE = (By.XPATH, '//input[@id="file-upload"]')
    UPLOAD = (By.XPATH, '//input[@id="file-submit"]')
    RED_SQUARE = (By.XPATH, '//div[@id="drag-drop-upload"]')
    UPLOADED_MSG = (By.XPATH, '//h3[contains(text(),"File Uploaded!")]')

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element(*self.UPLOAD_PAGE).click()

    def tearDown(self):
        self.driver.quit()

    def test_visible_upload(self):
        self.driver.find_element(*self.CHOOSE_FILE).send_keys(
            "C:/Users/Maria/PycharmProjects/Tests_Heroku_Internet/assets/cat.jpg")
        self.driver.find_element(*self.UPLOAD).click()
        expected = self.driver.find_element(*self.UPLOADED_MSG).text
        time.sleep(4)
        self.assertIn('File Uploaded!', expected, 'File not uploaded')


