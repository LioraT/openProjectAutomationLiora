import requests
from requests.auth import HTTPBasicAuth
from framework.api.work_packages_api import WorkPackagesApi
from configurations.api_config import config
from utils.data_generator import DataGenerator
import pytest
from allure_commons._allure import step


@step("api test - Update work package")
def test_006_api_update_work_package():

    work_package_id = 243

    work_packages_api = WorkPackagesApi(config['base_url'])
    work_package = work_packages_api.get_work_package(work_package_id)

    updated_description = "Updated work package description:" + DataGenerator.random_generator(3)

    payload = {
        "lockVersion": work_package["lockVersion"],
        "_links": {},
        "description": {
            "raw": updated_description
        }
    }

    work_package = work_packages_api.update_work_package(work_package_id, payload)

    assert work_package["description"]["raw"] == updated_description, \
        f"expected work package description: '{updated_description}'"
