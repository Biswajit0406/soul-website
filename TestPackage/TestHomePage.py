import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import webdriver
import time
from UtilityPackage.ReadConfigFile import ReadConfigClass
from PageObjectPackage.PageObjectHomePage import HomePage
from UtilityPackage.custom_logger import Logger


class TestHomePage:
    url = ReadConfigClass.get_url()
    logger = Logger.log()

    def test_logo(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.hp = HomePage(self.driver)
        self.hp.logo_test()
        self.logger.info("******************************** Test case passed ***********************************")
        self.driver.save_screenshot("C:/Users/KIIT/PycharmProjects/Soul_Website/screenshots/screenshot2.png")
        self.driver.close()
