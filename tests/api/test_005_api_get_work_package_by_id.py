import requests
from requests.auth import HTTPBasicAuth
from framework.api.projects_api import ProjectsApi
from framework.api.work_packages_api import WorkPackagesApi
from configurations.api_config import config
import pytest
from allure_commons._allure import step


@step("api test - Create work package id")
def test_005_api_get_work_package_by_id():

    work_package_id = 243
    expected_work_package_type = "Task"
    expected_work_package_subject = "My Task 1"

    work_packages_api = WorkPackagesApi(config['base_url'])
    work_package = work_packages_api.get_work_package(work_package_id)

    work_package_type = work_package["_embedded"]["type"]["name"]
    work_package_subject = work_package["subject"]

    assert work_package_type == expected_work_package_type, \
        f"expected work package type: '{expected_work_package_type}'"
    assert work_package_subject == expected_work_package_subject, \
        f"expected work package subject: '{expected_work_package_subject}'"
