import requests
import json
from http import HTTPStatus


class RestClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path, basic_auth, expected_response_status_code: int = HTTPStatus.OK):
        url = self.base_url + path
        response = requests.get(url, auth=basic_auth)
        assert response.status_code == expected_response_status_code, \
            f"\"GET\": {url}\nBad Response: {response} "
        return response

    def patch(self, path, basic_auth, content_type, payload, expected_response_status_code: int = HTTPStatus.OK):
        url = self.base_url + path
        request_body = json.dumps(payload)
        response = requests.patch(url, data=request_body, auth=basic_auth, headers=content_type)
        assert response.status_code == expected_response_status_code, \
            f"\"PATCH\": {url}\nBad Response: {response}"
        return response
    
    def post(self, path, basic_auth, content_type, payload, expected_response_status_code: int = HTTPStatus.OK):
        url = self.base_url + path
        request_body = json.dumps(payload)
        response = requests.post(url, data=request_body, auth=basic_auth, headers=content_type)
        assert response.status_code == expected_response_status_code, \
            f"\"POST\": {url}\nBad Response: {response}"
        return response

    def delete(self, path, basic_auth, content_type, expected_response_status_code: int = HTTPStatus.OK):
        url = self.base_url + path
        response = requests.delete(url, auth=basic_auth, headers=content_type)
        assert response.status_code == expected_response_status_code, \
            f"\"DELETE\": {url}\nBad Response: {response}"
        return response

