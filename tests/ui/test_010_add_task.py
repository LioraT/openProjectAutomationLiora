import time
import pytest
from allure_commons._allure import step
from framework.utils.shared_steps import SharedSteps
from framework.page_objects.dashboard_page import DashboardPage
from framework.page_objects.work_packages_page import ProjectWorkPackagesPage
from framework.page_objects.project_overview_page import ProjectOverviewPage
from utils.data_generator import DataGenerator
from utils.read_properties import ReadConfig
from tests.ui.conf_test import setup


@step("Create Task Test")
@pytest.mark.sanity
@pytest.mark.regression
def test_addTask(setup):
    specific_project_name = "TestProject1"
    max_rows_in_page = 20
    task_subject = "Task Subject" + DataGenerator.random_generator(3)
    task_description = "Task Description" + DataGenerator.random_generator(3)

    driver = setup
    driver.get(ReadConfig.getApplicationURL())

    SharedSteps.login_steps(driver)
    dashboard = DashboardPage(driver)
    dashboard.click_on_search_dropdown()
    dashboard.click_on_project_name_in_search_dropdown(specific_project_name)
    project_on_top_left_corner = dashboard.get_project_name_on_top_left_corner()
    assert specific_project_name == project_on_top_left_corner

    project_overview = ProjectOverviewPage(driver)
    project_overview.click_on_wp_on_side_bar()
    work_packages = ProjectWorkPackagesPage(driver)

    last_row_number_before_adding_task = int(work_packages.get_table_rows_total_number())

    work_packages.click_on_wp_plus_create_menu()
    work_packages.click_on_wp_option_in_plus_create_menu("Task")
    nt_title = work_packages.verify_work_package_window_title("New", "Task")
    assert nt_title == True, "'New Task' title in create task inner pop up"

    work_packages.set_subject(task_subject)
    work_packages.set_description_xpath(task_description)
    work_packages.click_save_button()
    work_packages.close_inner_window()

    last_row_number_after_adding_task = int(work_packages.get_table_rows_total_number())

    assert (last_row_number_before_adding_task + 1) == last_row_number_after_adding_task, \
        "number of rows after adding work package should be plus one"

    row_page_num = work_packages.get_row_page_number(max_rows_in_page, last_row_number_after_adding_task)
    row_location_in_current_page = work_packages.get_row_location_in_current_page(max_rows_in_page,
                                                                                  last_row_number_after_adding_task)

    if row_page_num > 1:
        work_packages.click_table_page_number(row_page_num)

    time.sleep(1)
    added_task_subject = work_packages. \
        get_value_from_parameter_of_row_in_page(row_location_in_current_page, "subject")

    assert added_task_subject == task_subject, "the added subject is " + added_task_subject

    added_task_type = work_packages. \
        get_value_from_parameter_of_row_in_page(row_location_in_current_page, "type")

    assert added_task_type == 'TASK', "the added type is " + added_task_type
