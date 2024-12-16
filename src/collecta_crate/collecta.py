import requests

from .endpoints.auth import Auth
from .endpoints.files import Files
from .endpoints.search import Search
from .endpoints.objects import Objects


class Collecta:

    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({"Authorization": f"Bearer {api_key}"})
        self.objects = Objects(self)
        self.files = Files(self)
        self.search = Search(self)
        self.auth = Auth(self)

    def request(self, method, endpoint, params=None, data=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.request(method, url, params=params, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def get(self, endpoint, params=None, headers=None):
        return self.request("GET", endpoint, params=params, headers=headers)

    def post(self, endpoint, data=None, headers=None):
        return self.request("POST", endpoint, data=data, headers=headers)

    def put(self, endpoint, data=None, headers=None):
        return self.request("PUT", endpoint, data=data, headers=headers)

    def delete(self, endpoint, headers=None):
        return self.request("DELETE", endpoint, headers=headers)

