__author__ = 'kzv'
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from devmate.pages.home_page import HomePage
from devmate.pages.signup_page import SignUpPage
from devmate.pages.frameworks_page import FrameworksPage
from devmate.pages.app_management_page import AppManagementPage
import os
import sys

class Application(object):

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)
        self.home_page = HomePage(driver, base_url)
        self.signup_page = SignUpPage(driver, base_url)
        self.frameworks_page = FrameworksPage(driver, base_url)
        self.app_management_page = AppManagementPage(driver, base_url)

    def go_to_home_page(self):
        self.driver.get(self.base_url)

    def go_to_signup_page(self):
        self.home_page.signup_button.click()

    def check_outside_checkbox(self):
        self.signup_page.selling_outside_checkbox.click()

    def take_page_screenshot(self):
        target= open('/home/kzv/ololol','w')
        target.write(os.path.abspath(__file__))
        self.driver.save_screenshot('./screen.png')