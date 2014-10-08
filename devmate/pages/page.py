__author__ = 'kzv'
from selenium.webdriver.support.expected_conditions import *

class Page(object):

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url


    def is_element_visible(self, locator):
        try:
            return self.wait.until(visibility_of_element_located(locator))
        except WebDriverException:
            return False

    def is_it_page_url(self, url):
        if self.driver.current_url() == url:
            return True
        else:
            return False