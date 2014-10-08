__author__ = 'kzv'
from devmate.pages.page import Page

class SignUpPage(Page):

    @property
    def selling_outside_checkbox(self):
        return self.driver.find_element_by_xpath(".//input[@name='selling_outside_app_store']")

    @property
    def solution_field(self):
        return self.driver.find_element_by_xpath(".//input[@name='solution']")