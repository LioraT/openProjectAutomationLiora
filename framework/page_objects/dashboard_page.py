from framework.page_objects.wrapper import SeleniumWrapper
from selenium.webdriver.common.by import By
from framework.utils.element_locator import ElementLocator as el
from allure_commons._allure import step


class DashboardPage(SeleniumWrapper):
    linkbtn_plus_xpath = el(By.XPATH, "//*[contains(@class, 'quick-add-menu--button')]")
    linkbtn_addProject_xpath = el(By.XPATH, "//a[@aria-label='New project']")
    linkbtn_selectProject_id = el(By.ID, "projects-menu")
    txt_project_name_xpath = el(By.XPATH, "//a[@span_class ='op-app-menu--item-title ellipsis']")
    txt_projectSearch_id = el(By.ID, "projects-menu")
    txt_projectInList_xpath_locator_value = "//li[@class='ui-matched-item ui-menu-item']/div/a[text()='{0}']"
    lnkbtn_projectSearch_a = el(By.LINK_TEXT, "/projects/demo-project")


    def __init__(self, driver):
        self.driver = driver

    @step("click select project drop down")
    def click_on_select_a_project_dropdown(self):
        self.click(self.linkbtn_selectProject_id)

    @step("get project name in top left corner")
    def get_project_name_on_top_left_corner(self):
        return self.get_element(self.txt_project_name_xpath).get_attribute('title')

    @step("open search drop down")
    def click_on_search_dropdown(self):
        self.click(self.txt_projectSearch_id)

    @step("choose project name from search drop down")
    def click_on_project_name_in_search_dropdown(self, project_name_to_search):
        locator_value = self.txt_projectInList_xpath_locator_value.format(project_name_to_search)
        self.click(el(By.XPATH, locator_value))

    @step("click the plus button")
    def click_on_plus_button(self):
        self.click(self.linkbtn_plus_xpath)

    @step("click the add project in the plus button")
    def click_on_add_project_in_plus_options(self):
        self.click(self.linkbtn_addProject_xpath)


