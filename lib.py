from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

def _wait(fun):
    def wrapper(*args, **kwargs):
        instance, locator = args
        w = WebDriverWait(instance.driver, 10)
        v = visibility_of_element_located(locator)
        w.until(v,message = f"Element not found {locator}")
        return fun(*args, **kwargs)
    return wrapper

def wait_cls(cls):
    for key, val in cls.__dict__.items():
        if callable(val) and key != "__init__":
            setattr(cls, key, _wait(val))
    return  cls

class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def enter_text(self, locator, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    def select_item(self, locator, item):
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(item)


