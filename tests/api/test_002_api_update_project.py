import requests
from requests.auth import HTTPBasicAuth
from framework.api.projects_api import ProjectsApi
from configurations.api_config import config
from utils.data_generator import DataGenerator
import pytest
from allure_commons._allure import step


@step("api test - Update project")
def test_002_api_update_project():
    updated_project_description = "Updated Project description:" + DataGenerator.random_generator(3)
    # updated_project_description = "This is the first test project"

    projects_api = ProjectsApi(config['base_url'])
    project_id = config['project_id']

    payload = {
        "_links": {},
        "description": {
            "raw": updated_project_description
        }
    }
    project = projects_api.update_project(project_id, payload)

    assert project["description"]["raw"] == updated_project_description, \
        f"expected updated project description: '{updated_project_description}'"
