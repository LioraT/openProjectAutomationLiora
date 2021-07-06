import requests
from requests.auth import HTTPBasicAuth
from framework.api.projects_api import ProjectsApi
from configurations.api_config import config
from utils.data_generator import DataGenerator
import time
import pytest
from allure_commons._allure import step


@step("api test - Delete project")
def test_004_api_delete_project():
    random_number = DataGenerator.random_generator(3)
    new_project_name = f"NewProject{random_number}"
    new_project_identifier = f"new_identifier{random_number}"

    projects_api = ProjectsApi(config['base_url'])

    payload = {
        "name": new_project_name,
        "identifier": new_project_identifier
    }

    # Creating a new product for later deletion
    project = projects_api.create_project(payload)

    assert project["name"] == new_project_name,\
        f"the added project name for deletion: '{new_project_name}'"

    new_project_id = project["id"]

    # Deleting the product
    projects_api.delete_project(new_project_id)

    # Checking (after a moment) that the product was deleted
    # by getting 404 response on a get request for this product
    time.sleep(4)
    projects_api.get_project(new_project_id, expected_response_status_code=404)


