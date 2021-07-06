import requests
from requests.auth import HTTPBasicAuth
from framework.api.projects_api import ProjectsApi
from configurations.api_config import config
import pytest
from allure_commons._allure import step


@step("api test - Get project id")
def test_001_get_project_by_id():
    expected_project_name = "TestProject1"
    expected_project_description = "This is the first test project"

    projects_api = ProjectsApi(config['base_url'])
    project_id = config['project_id']

    project = projects_api.get_project(project_id)

    assert project["name"] == expected_project_name,\
        f"expected project name: '{expected_project_name}'"
    assert project["description"][
               "raw"] == expected_project_description,\
        f"expected project description: '{expected_project_description}'"
