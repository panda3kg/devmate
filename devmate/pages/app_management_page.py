__author__ = 'kzv'
from devmate.pages.features_navigation_menu import FeatureMenu

class AppManagementPage(FeatureMenu):

    @property
    def img__easy_update(self):
        return self.driver.find_element_by_xpath("//img[@alt='Easy Updates']")