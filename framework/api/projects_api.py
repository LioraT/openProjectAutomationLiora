from http import HTTPStatus
from configurations.api_config import config
from framework.api.rest_client import RestClient
from requests.auth import HTTPBasicAuth


class ProjectsApi(RestClient):

    def __init__(self, base_url):
        self.base_url = base_url
        self.basic_auth = HTTPBasicAuth(config['basic_auth']['username'], config['basic_auth']['password'])
        self.content_type = {'Content-Type': 'application/json'}

    def get_project(self, project_id, expected_response_status_code: int = HTTPStatus.OK):
        response = self.get(path=f"/api/v3/projects/{project_id}",
                            basic_auth=self.basic_auth,
                            expected_response_status_code=expected_response_status_code)
        return response.json()

    def create_project(self, payload):
        response = self.post(path=f"/api/v3/projects", payload=payload,
                             basic_auth=self.basic_auth, content_type=self.content_type,
                             expected_response_status_code=HTTPStatus.CREATED)
        return response.json()

    def update_project(self, project_id, payload):
        response = self.patch(path=f"/api/v3/projects/{project_id}", payload=payload,
                              basic_auth=self.basic_auth, content_type=self.content_type)
        return response.json()

    def delete_project(self, project_id):
        self.delete(path=f"/api/v3/projects/{project_id}",
                    basic_auth=self.basic_auth, content_type=self.content_type,
                    expected_response_status_code=HTTPStatus.NO_CONTENT)
