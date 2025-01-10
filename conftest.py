from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver as FireFox
from pytest import fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", dest="browser", default="chrome")
    parser.addoption("--env", action="store", dest="env", default="test")
    parser.addoption("--timeout", action="store", dest="timeout", default=10)

class TestConfigurations:
    url = "https://demowebshop.tricentis.com/"
    email = "hello.world@company.com"
    password = "Password123"
    agent_id =12345

class StageConfigurations:
    url = "https://demowebshop.tricentis.com/"
    email = "bill.gates@company.com"
    password = "Password123"
    agent_id = 89989

@fixture
def _config(request):
    env = request.config.option.env.upper()
    if env == "TEST":
        print("Test Environment")
        return TestConfigurations
    elif env == "STAGE":
        print("Stage Environment")
        return StageConfigurations
    else:
        raise Exception("Unknown Environment")

@fixture
def _driver(_config, request):
    browser = request.config.option.browser.upper()
    if browser == 'CHROME':
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options= opt)
    elif browser == "FIREFOX":
        driver = FireFox()
    elif browser == "EDGE":
        opt = webdriver.EdgeOptions()
        opt.add_experimental_option('detach', True)
        driver = webdriver.Edge(options=opt)
    else:
        raise Exception(f"Browser {browser} is not supported ")

    driver.maximize_window()
    driver.get(_config.url)
    yield driver
    driver.close()
