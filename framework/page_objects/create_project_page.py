from framework.page_objects.wrapper import SeleniumWrapper
from selenium.webdriver.common.by import By
from framework.utils.element_locator import ElementLocator as el
from allure_commons._allure import step


class CreateProject(SeleniumWrapper):

    txt_projectName_xpath = el(By.XPATH, "//input[@id='formly_3_textInput_name_0']")
    btn_advancesSettingSection_class = el(By.CLASS_NAME, "op-fieldset--toggle")
    txt_advancedSettingsDescription_class = el(By.CLASS_NAME, "op-uc-p")
    dd_status_xpath = el(By.XPATH, "//*[contains(@id,'StatusInput__links.status_4')]//input")
    dd_Status_options_xpath_locator_value = "//div[@role='option' and .//span[.='{0}']]"
    btn_saveNewProject_xpath = el(By.XPATH, "//button[@type='submit'][@class='button -highlight']")

    def __init__(self, driver):
        self.driver = driver

    @step("set project name")
    def set_project_name(self, project_name):
        self.send_keys(self.txt_projectName_xpath, project_name)

    @step("click the advanced setting section")
    def click_on_advanced_settings_section(self):
        self.click(self.btn_advancesSettingSection_class)

    @step("set the advanced setting description")
    def set_advanced_settings_description(self, description):
        self.send_keys(self.txt_advancedSettingsDescription_class, description)

    @step("open status drop down")
    def open_status_dropdown(self):
        self.click(self.dd_status_xpath)

    @step("select status option from drop down")
    def select_status_dropdown_option(self, status_option):
        locator_value = self.dd_Status_options_xpath_locator_value.format(status_option)
        self.click(el(By.XPATH, locator_value))

    @step("click save button")
    def click_save_button(self):
        self.click(self.btn_saveNewProject_xpath)
