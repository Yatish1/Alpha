from lib import SeleniumWrapper
from homepage import HomePage
from excel import read_locators
from pytest import mark



class RegistrationPage:
    _locators = read_locators('registrationpage')

    # _rdo_male = ("id", "gender-male")
    # _rdo_female = ("id", "gender-female")
    # _txt_fname = ("id", "FirstName")
    # _txt_lname = ("id", "LastName")
    # _txt_email = ("id", "Email")
    # _txt_password = ("id", "Password")
    # _txt_confirm_password = ("id", "ConfirmPassword")
    # _btn_register = ("xpath", "//input[@id='register-button']")

    def __init__(self, driver):
        self.driver = driver

    def register(self, gender, fname, lname, email, password, confirmpassword):
        s = SeleniumWrapper(self.driver)
        homepage = HomePage(self.driver)
        homepage.click_register()

        if gender.upper() == "MALE":
            s.click_element(self._locators['rdo_male'])
        elif gender.upper() == "FEMALE":
            s.click_element(self._locators['rdo_female'])
        else:
            raise Exception("Unknown Gender")
        s.enter_text(self._locators['txt_fname'], value = fname)
        s.enter_text(self._locators['txt_lname'], value = lname)
        s.enter_text(self._locators['txt_email'], value = email)
        s.enter_text(self._locators['txt_password'], value = password)
        s.enter_text(self._locators['txt_confirmpassword'], value = password)
        s.click_element(self._locators['btn_register'])
