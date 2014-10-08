__author__ = 'kzv'
from selenium.webdriver.support.select import Select
from  devmate.conftest import app

def test_first(app):
    app.go_to_home_page()
    app.go_to_signup_page()
    app.check_outside_checkbox()
    app.take_page_screenshot()