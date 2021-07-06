import requests
from requests.auth import HTTPBasicAuth
from framework.api.work_packages_api import WorkPackagesApi
from configurations.api_config import config
from utils.data_generator import DataGenerator
import pytest
from allure_commons._allure import step


@step("api test - Delete work package")
def test_008_api_delete_work_package():
    work_packages_api = WorkPackagesApi(config['base_url'])
    new_work_package_subject = "Unique task subject " + DataGenerator.random_generator(3)

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

    # Creating a new work package for later deletion
    work_package = work_packages_api.create_work_package(payload)

    new_work_package_id = work_package["id"]

    # Deleting the work package
    work_packages_api.delete_work_package(new_work_package_id)

    # Checking that the work package was deleted
    # by getting 404 response on a get request for this product
    work_packages_api.get_work_package(new_work_package_id, expected_response_status_code=404)
