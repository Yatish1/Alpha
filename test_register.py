from lib import SeleniumWrapper
from pytest import mark
from registration import RegistrationPage
from homepage import HomePage
from excel import read_headers, read_data

headers = read_headers("test_registration", "smoke")
data = read_data("test_registration", "smoke")

@mark.parametrize(headers, data)
def test_register(_driver, gender, fname, lname, email, password, confirmpassword):
    # s = SeleniumWrapper(_driver)
    homepage = HomePage(_driver)
    homepage.click_register()
    registerpage = RegistrationPage(_driver)
    registerpage.register(gender, fname,lname, email, password, confirmpassword)
