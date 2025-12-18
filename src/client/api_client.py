import requests
from src.utils.conftest import Configuration


class ApiClient:
    def __init__(self):
        self.url = Configuration.URL.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })

    def _build_url(self, endpoint):
        endpoint = endpoint.lstrip('/')
        return f"{self.url}/{endpoint}"

    def get_token(self, endpoint, body=None):
        try:
            url = self._build_url(endpoint)
            response = self.session.post(url, json=body)
            token = response.json()["access_token"]
            if token:
                headers = {"Authorization": f"Bearer {token}"}
                self.session.headers.update(headers)
                return headers
            return None
        except requests.exceptions.RequestException as e:
            raise Exception(f"Token request failed: {e}")

    def admin_token(self, endpoint, body=None):
        res = self.get_token(endpoint, body)
        return res

    def user_token(self, endpoint, body=None):
        res = self.get_token(endpoint, body)
        return res

    def get(self, endpoint):
        try:
            url = self._build_url(endpoint)
            return self.session.get(url)
        except requests.exceptions.RequestException as e:
            raise Exception(f"GET request failed: {e}")

    def post(self, endpoint, body=None, headers=None):
        try:
            url = self._build_url(endpoint)
            return self.session.post(url, json=body, headers=headers)
        except requests.exceptions.RequestException as e:
            raise Exception(f"POST request failed: {e}")

    def put(self, endpoint, body=None):
        try:
            url = self._build_url(endpoint)
            return self.session.put(url, json=body)
        except requests.exceptions.RequestException as e:
            raise Exception(f"PUT request failed: {e}")

    def delete(self, endpoint):
        try:
            url = self._build_url(endpoint)
            return self.session.delete(url)
        except requests.exceptions.RequestException as e:
            raise Exception(f"DELETE request failed: {e}")