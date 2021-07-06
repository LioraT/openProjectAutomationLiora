from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from framework.utils.element_locator import ElementLocator as el


class SeleniumWrapper:
    driver: WebDriver
    actions: WebDriver

    def __init__(self, driver):
        self.driver: webdriver = driver
        self.actions = ActionChains(driver)

    def click(self, locator: el):
        element = self.get_element(locator)
        element.click()

    def send_keys(self, locator: el, text):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: el) -> str:
        element = self.get_element(locator, False)
        element_text = element.text
        return element_text

    def get_elements(self, locator: el) -> [WebElement]:
        elements = self.driver.find_elements(locator.by, locator.value)
        return elements

    def get_element(self, locator: el, until_visible: bool = True) -> WebElement:
        if until_visible:
            return self.wait_until_element_visibility(locator)
        else:
            return self.wait_until_element_presence(locator)

    def wait_until_element_visibility(self, locator: el) -> WebElement:
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((locator.by, locator.value)))
        return element

    def wait_until_element_presence(self, locator: el) -> WebElement:
        element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((locator.by, locator.value)))
        return element
