import requests
from requests.auth import HTTPBasicAuth
from framework.api.work_packages_api import WorkPackagesApi
from configurations.api_config import config
from utils.data_generator import DataGenerator
import pytest
from allure_commons._allure import step


@step("api test - Create work package")
def test_007_api_create_work_package():

    work_packages_api = WorkPackagesApi(config['base_url'])
    new_work_package_subject = "Unique task subject " + DataGenerator.random_generator(3)
    # new_work_package_subject = "My Task 1"
    payload = {
        "subject": new_work_package_subject,
        "_links": {
            "project": {
                "href": f"/api/v3/projects/{config['project_id']}",
                "title": config['project_name']
            },
            "type": {"href": "/api/v3/types/1", "title": "Task"},
            "assignee": {"href": None},
        }
    }

    work_package = work_packages_api.create_work_package(payload)

    assert work_package["subject"] == new_work_package_subject, \
        f"expected new work package subject: '{new_work_package_subject}'"
