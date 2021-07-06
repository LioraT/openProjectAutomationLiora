import time
import pytest
from allure_commons._allure import step
from framework.page_objects.create_project_page import CreateProject
from framework.page_objects.dashboard_page import DashboardPage
from utils.data_generator import DataGenerator
from utils.read_properties import ReadConfig
from framework.utils.shared_steps import SharedSteps
from tests.ui.conf_test import setup


@step("Create Project Test")
@pytest.mark.sanity
@pytest.mark.regression
def test_addProject(setup):
    expected_title = "New project | OpenProject"
    driver = setup
    driver.get(ReadConfig.getApplicationURL())
    SharedSteps.login_steps(driver)
    dashboard = DashboardPage(driver)
    dashboard.click_on_plus_button()
    dashboard.click_on_add_project_in_plus_options()
    cp_title = driver.title

    # time.sleep(1)
    assert cp_title == expected_title, \
        f"actual page title is: {cp_title} , while expected is: {expected_title}"

    create_project = CreateProject(driver)
    project_name = "NewProject" + DataGenerator.random_generator(3)
    create_project.set_project_name(project_name)
    create_project.click_on_advanced_settings_section()
    create_project.set_advanced_settings_description("descriptiontext")
    create_project.open_status_dropdown()
    create_project.select_status_dropdown_option(ReadConfig.getStatusOnTrack())
    create_project.click_save_button()
    dashboard = DashboardPage(driver)

    time.sleep(1)
    project_name_from_menu = dashboard.get_project_name_on_top_left_corner()
    assert project_name_from_menu == project_name,\
        f"actual project name is: {project_name_from_menu} , while expected is: {project_name}"





