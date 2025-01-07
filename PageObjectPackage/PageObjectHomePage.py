from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import webdriver
import time


who_we_are_xpath = "//button[normalize-space()='Who we are?']"
our_vision_mission_xpath = "//button[normalize-space()='Our Vision & Mission']"
our_values_xpath = "//button[normalize-space()='Our Values']"
about_us_xpath = "//a[contains(@class,'drop-down')][normalize-space()='About Us']"
company_logo_xpath = "//img[@alt='Company Logo']"
your_full_name_xpath = "//input[@placeholder='Your Full Name']"
your_email_xpath = "//input[@placeholder='Your Email']"
your_contact_number_xpath = "//input[@placeholder='Your Contact Number']"
write_your_meassage_xpath = "//textarea[@id='msg-text']"

class HomePage:
    logo_xpath = "//img[@alt='Company Logo']"
    def __init__(self,driver):
        self.driver = driver
    def logo_test(self):
        logo=self.driver.find_element(By.XPATH,self.logo_xpath)

        expected_url="https://soulltd.in/"
        actual_url=self.driver.current_url
        assert expected_url == actual_url,f"The urls are not getting matched"





