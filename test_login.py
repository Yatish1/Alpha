from lib import SeleniumWrapper
from pytest import mark
from loginpage import LoginPage
from homepage import HomePage
from excel import read_data, read_headers

headers = read_headers("test_login_positive", "smoke")
data = read_data("test_login_positive", "smoke")

@mark.parametrize(headers, data)
def test_login_positive(_driver, email, password):
    s = SeleniumWrapper(_driver)
    homepage = HomePage(_driver)
    homepage.click_login()
    loginpage = LoginPage(_driver)
    loginpage.login(email, password)

def test_login_negative(_driver):
    s = SeleniumWrapper(_driver)
    homepage = HomePage(_driver)
    homepage.click_login()
    loginpage = LoginPage(_driver)
    loginpage.login("hello.world@compnay.com", "Password12")