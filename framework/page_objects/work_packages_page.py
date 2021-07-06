import time

from framework.page_objects.wrapper import SeleniumWrapper
from selenium.webdriver.common.by import By
from framework.utils.element_locator import ElementLocator as el
from selenium.common.exceptions import NoSuchElementException
import re
from allure_commons._allure import step


class ProjectWorkPackagesPage(SeleniumWrapper):
    workpackages_num_of_rows_in_table = 0
    tblr_WorkPackages_xpath_locator_value = "//tbody[contains(@class,'results-tbody')]/tr"
    tblr_c_WorkPackages_xpath_locator_value = tblr_WorkPackages_xpath_locator_value + \
                                              "[{0}]/td/span[contains(@class,'{1}')]"
    linkbtn_plusCreate_xpath = el(By.XPATH, "//div[@class='wp-create-button']//button")
    tblr_plusCreateOptions_xpath_locator_value = "//ul[@class='dropdown-menu']//li//a//span[contains(text(),'{0}')]"

    title_newTaskWindowTitle_xpath_locator_value = "//div[contains(@class,'--details-content')]" \
                                                   "//span[contains(text(),'{0}')]"
    new_task_title = "New Task"

    txtbx_Subject_xpath = el(By.XPATH, "//input[@id='wp-new-inline-edit--field-subject']")
    txtDescription_xpath = el(By.XPATH, "//div[contains(@class,'editable op-uc-container')]")
    linkbtn_save_new_task_xpath = el(By.XPATH, "//button[@id='work-packages--edit-actions-save']")
    btn_close_inner_window_xpath = el(By.XPATH, "//span[@class='icon-context icon-close']")
    btn_next_xpath = el(By.XPATH, "//ul//li[contains(@class,'pagination--item')]//"
                                  "a[contains(@class,'pagination--next-link')]")
    btn_prev_xpath = el(By.XPATH, "//ul//li[contains(@class,'pagination--item')]//"
                                  "a[contains(@id,'pagination--prev-link')]")
    total_rows_in_tbl_xpath = el(By.XPATH, "//li[@class='pagination--range']")
    lnkbtn_page_number_xpath_locator_value = "//a[@role='link'][contains(text(),'{0}')]"
    txt_emptyAllOpenTable_id = el(By.ID, "empty-row-notification")

    def __init__(self, driver):
        self.driver = driver

    def click_table_page_number(self, page_number_to_go_to):
        try:
            locator_value = self.lnkbtn_page_number_xpath_locator_value.format(page_number_to_go_to)
            self.click(el(By.XPATH, locator_value))
        except NoSuchElementException:
            return

    def get_table_rows_total_number(self):
        time.sleep(1)
        elements_list = self.get_elements(self.txt_emptyAllOpenTable_id)
        if len(elements_list) > 0:
            return 0
        try:
            text = self.get_text(self.total_rows_in_tbl_xpath)
            res = re.findall(r"\d+", text)
            return res[2]
        except NoSuchElementException:
            return 0

    def get_row_page_number(self, max_rows_in_page, row_number):
        return (row_number // max_rows_in_page) + 1

    def get_row_location_in_current_page(self, max_rows_in_page, row_number):
        res = row_number % max_rows_in_page
        if res == 0:
            return 20
        else:
            return res

    @step("get the value of a parameter in a specific row in the table")
    def get_value_from_parameter_of_row_in_page(self, row_location_in_current_page, table_parameter):
        # extracting the parameter value from the specific row
        locator_value = self.tblr_c_WorkPackages_xpath_locator_value.format(row_location_in_current_page,
                                                                            table_parameter)
        return self.get_text(el(By.XPATH, locator_value))

    @step("click '+Create' button in Work s Page")
    def click_on_wp_plus_create_menu(self):
        self.click(self.linkbtn_plusCreate_xpath)

    @step("click the 'TASK' option in Work Packages Page")
    def click_on_wp_option_in_plus_create_menu(self, work_package_option):
        locator_value = self.tblr_plusCreateOptions_xpath_locator_value.format(work_package_option)
        self.click(el(By.XPATH, locator_value))

    @step("verify the work package inner window title appear")
    def verify_work_package_window_title(self, wp_status, wp_type):
        locator_value = self.title_newTaskWindowTitle_xpath_locator_value.format(wp_status)
        is_element_exist = self.get_element(el(By.XPATH, locator_value)).is_displayed()
        locator_value = self.title_newTaskWindowTitle_xpath_locator_value.format(wp_type)
        is_element_exist += self.get_element(el(By.XPATH, locator_value)).is_displayed()
        return is_element_exist is not None

    @step("set subject")
    def set_subject(self, subject):
        self.send_keys(self.txtbx_Subject_xpath, subject)

    @step("set description")
    def set_description_xpath(self, description):
        self.send_keys(self.txtDescription_xpath, description)

    @step("click 'Save'")
    def click_save_button(self):
        self.click(self.linkbtn_save_new_task_xpath)

    @step("close inner window")
    def close_inner_window(self):
        self.click(self.btn_close_inner_window_xpath)
