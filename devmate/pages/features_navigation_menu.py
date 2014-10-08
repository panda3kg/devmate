__author__ = 'kzv'
from devmate.pages.page import Page

class FeatureMenu(Page):

    @property
    def frameworks_menu_item(self):
        return self.driver.find_element_by_xpath("//span[@class='i-tab-frameworks']")

    @property
    def app_management__menu_item(self):
        return self.driver.find_element_by_xpath("//span[@class='i-tab-app-management']")