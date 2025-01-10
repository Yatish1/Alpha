from lib import SeleniumWrapper
from excel import read_locators

class LoginPage:
    _locators = read_locators("loginpage")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        s = SeleniumWrapper(self.driver)
        s.enter_text(self._locators["txt_email"], value=username)
        s.enter_text(self._locators["txt_password"], value=password)
        s.click_element(self._locators["btn_login"])
