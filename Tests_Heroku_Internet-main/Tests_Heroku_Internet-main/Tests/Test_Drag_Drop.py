import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DragDrop(unittest.TestCase):
    DRAG_DROP_PG = (By.XPATH, '//a[contains(text(),"Drag")]')
    FIRST = (By.XPATH, '//div[@id="column-a"]')
    SECOND = (By.XPATH, '//div[@id="column-b"]')

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://the-internet.herokuapp.com")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.find_element(*self.DRAG_DROP_PG).click()

    def tearDown(self):
        self.driver.quit()

    def test_dragA_drop_onB(self):
        actions = ActionChains(self.driver)
        source = self.driver.find_element(*self.FIRST)
        target = self.driver.find_element(*self.SECOND)
        actions.click_and_hold(source).move_to_element_with_offset(target, 150, 100).perform()
        result = self.driver.find_element(By.XPATH, '//div[@id="column-b"]//parent::header').text
        self.assertIn('A', result, 'Action not performed')
