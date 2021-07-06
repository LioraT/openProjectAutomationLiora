from framework.page_objects.wrapper import SeleniumWrapper
from selenium.webdriver.common.by import By
from framework.utils.element_locator import ElementLocator as el
from allure_commons._allure import step


class ProjectOverviewPage(SeleniumWrapper):
    lstmnu_sideBar_xpath_locator_value = "//ul[contains(@class,'menu_root open')]//li//div//a[@title='{}']"

    def __init__(self, driver):
        self.driver = driver

    @step("click on work packages option on the side bar")
    def click_on_wp_on_side_bar(self):
        locator_value = self.lstmnu_sideBar_xpath_locator_value.format('Work packages')
        self.click(el(By.XPATH, locator_value))
