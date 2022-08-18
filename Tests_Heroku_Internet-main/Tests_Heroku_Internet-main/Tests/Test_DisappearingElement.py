import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class DisappearingElement(unittest.TestCase):
    DISAPPEAR_PAGE = (By.XPATH, '//a[contains(text(),"Disappearing")]')
    HOME_BTN = (By.XPATH, '//a[contains(text(),"Home")]')
    ABOUT_BTN = (By.XPATH, '//a[contains(text(),"About")]')
    CONTACT_US_BTN = (By.XPATH, '//a[contains(text(),"Contact Us")]')
    PORTFOLIO_BTN = (By.XPATH, '//a[contains(text(),"Portfolio")]')
    GALLERY_BTN = (By.XPATH, '//a[contains(text(),"Gallery")]')

    NOT_FOUND_ERR = (By.XPATH, '/html/body/h1')

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element(*self.DISAPPEAR_PAGE).click()

    def tearDown(self):
        self.driver.quit()

    def not_found_err(self):
        error_msg = self.driver.find_element(*self.NOT_FOUND_ERR)
        self.assertIn(error_msg.text, 'Not Found', 'Not the correct error has been found!')

    def test_click_on_home_btn(self):
        self.driver.find_element(*self.HOME_BTN).click()
        actual = self.driver.current_url
        expected = 'https://the-internet.herokuapp.com/'
        self.assertEquals(expected, actual, "Failed! This is not home page!")

    def test_click_on_about_btn(self):
        self.driver.find_element(*self.ABOUT_BTN).click()
        self.not_found_err()

    def test_click_on_contact_us(self):
        self.driver.find_element(*self.CONTACT_US_BTN).click()
        self.not_found_err()

    def test_click_on_portfolio_btn(self):
        self.driver.find_element(*self.PORTFOLIO_BTN).click()
        self.not_found_err()

    def test_gallery_missing_page(self):
        expected = self.driver.find_element(*self.GALLERY_BTN).click()
        actual = 'Gallery'
        self.assertEqual(expected, actual, 'The gallery page is not found')
