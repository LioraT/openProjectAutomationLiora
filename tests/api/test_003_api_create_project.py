import requests
from requests.auth import HTTPBasicAuth
from framework.api.projects_api import ProjectsApi
from configurations.api_config import config
from utils.data_generator import DataGenerator
import pytest
from allure_commons._allure import step


@step("api test - Create project")
def test_003_api_create_project():
    random_number = DataGenerator.random_generator(3)
    new_project_name = f"NewProject{random_number}"
    new_project_identifier = f"new_identifier{random_number}"

    projects_api = ProjectsApi(config['base_url'])

    payload = {
        "name": new_project_name,
        "identifier": new_project_identifier
        }

    project = projects_api.create_project(payload)

    assert project["name"] == new_project_name, \
        f"expected new project: '{new_project_name}'"
    assert project["identifier"] == new_project_identifier, \
        f"expected project identifier: '{new_project_identifier}'"
