import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class ContextMenu(unittest.TestCase):
    BOX = (By.XPATH, '//*[@id="hot-spot"]')

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://the-internet.herokuapp.com/context_menu")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_box_select_box(self):
        action = ActionChains(self.driver)
        action.context_click(self.driver.find_element(*self.BOX)).perform()
        alert = self.driver.switch_to.alert
        print('', alert.text)
        self.assertEquals(alert.text, 'You selected a context menu', 'Failed to select context-menu alert!')
        alert.accept()


