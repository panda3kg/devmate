__author__ = 'kzv'
from devmate.pages.features_navigation_menu import FeatureMenu

class FrameworksPage(FeatureMenu):

    @property
    def img_update_framework(self):
        return self.driver.find_element_by_xpath("//img[@alt='Sparkle-based updates framework']")