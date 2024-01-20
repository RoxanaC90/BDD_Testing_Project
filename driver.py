from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from time import sleep


class Driver(unittest.TestCase):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.maximize_window()

    def close(self):
        sleep(3)
        self.driver.quit()
