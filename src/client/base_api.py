#from src.utils.conftest import Configuration
from src.client.api_client import ApiClient


class BaseApi(ApiClient):
    def __init__(self):
        super().__init__()  # initializes ApiClient

    def get(self, endpoint,headers=None):
        return super().get(endpoint)

    def post(self, endpoint, body=None,headers=None):
        return super().post(endpoint, body=body)

    def put(self, endpoint, body=None,headers=None):
        return super().put(endpoint, body)

    def delete(self, endpoint, headers=None):
        return super().delete(endpoint)
