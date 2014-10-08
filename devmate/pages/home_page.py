__author__ = 'kzv'

from devmate.pages.page import Page

class HomePage(Page):

    @property
    def signup_button(self):
        return self.driver.find_element_by_xpath("//a[@class='btn btn-construct btn-sign-up-now']")

