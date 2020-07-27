from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    driver = None
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
            self.driver.implicitly_wait(3)
        else:
            self.driver = driver
        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    # def wait_for_click(self, locator, time=10):
    #     WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))
    def wait_for_member(self, locator, time=10):
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))
