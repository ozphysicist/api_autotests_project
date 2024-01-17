from typing import Dict

import requests
from urllib3 import connection

from vars.envars import BASE_URL


class BaseApiClient:
    """Base API Client."""
    def __init__(self):
        """Constructor"""
        self.host = BASE_URL

    def request(self, method, url, body=None, headers=None):
        """Override default request method"""
        if headers is None:
            headers = {}
        else:
            # Avoid modifying the headers passed into .request()
            headers = headers.copy()
        super(connection.HTTPConnection, self).request(method, url, body=body, headers=headers)

    connection.HTTPConnection.request = request

    def get(self, path: str, auth: bool = False, headers: Dict = None, json: Dict = None,
            **kwargs) -> requests.Response:
        """GET request to API."""
        response = requests.get(url=self.host + path, auth=auth, headers=headers, json=json, **kwargs)
        return response

    def post(self, path: str, auth: bool = False, headers: Dict = None, json: Dict = None,
             **kwargs) -> requests.Response:
        """POST request to API."""
        response = requests.post(url=self.host + path, auth=auth, headers=headers, json=json, **kwargs)
        return response

    def put(self, path: str, auth: bool = False, headers: Dict = None, json: Dict = None,
            **kwargs) -> requests.Response:
        """PUT request to API."""
        response = requests.put(url=self.host + path, auth=auth, headers=headers, json=json, **kwargs)
        return response

    def patch(self, path: str, auth: bool = False, headers: Dict = None, json: Dict = None,
              **kwargs) -> requests.Response:
        """PATCH request to API."""
        response = requests.patch(url=self.host + path, auth=auth, headers=headers, json=json, **kwargs)
        return response

    def delete(self, path: str, auth: bool = False, headers: Dict = None, json: Dict = None,
               **kwargs) -> requests.Response:
        """DELETE request to API."""
        response = requests.delete(url=self.host + path, auth=auth, headers=headers, json=json, **kwargs)
        return response
