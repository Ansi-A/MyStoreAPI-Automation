import requests
from src.utils.conftest import Configuration

class ApiClient:
    def __init__(self):
        self.url= Configuration.URL
        self.session = requests.Session()
        self.session.headers.update({
        "Content-Type": "application/json"})

    def get_token(self,endpoint,body=None):
        try:
            response = self.session.post(self.url+endpoint,json=body)
            token = response.json()["access_token"]
            if token :
                headers={"Authorization":f"Bearer {token}"}
                self.session.headers.update(headers)
                return headers
            return None
        except requests.exceptions.RequestException as e:
            raise Exception(f"Token request failed: {e}")



    def admin_token(self,endpoint,body=None):

        res = self.get_token(endpoint, body)

        return res


    def user_token(self,endpoint,body=None):
        res = self.get_token(endpoint, body)
        return res

    def get(self,endpoint):
        try:
            return self.session.get(self.url+endpoint)
        except requests.exceptions.RequestException as e:
            raise Exception(f"GET request failed: {e}")

    def post(self,endpoint,body=None,headers=None):
        try:
            return self.session.post(self.url+endpoint,json=body,headers=headers)
        except requests.exceptions.RequestException as e:
            raise Exception(f"POST request failed: {e}")

    def put(self,endpoint,body=None):
        try:
            return self.session.put(self.url+endpoint,json=body)
        except requests.exceptions.RequestException as e:
            raise Exception(f"PUT request failed: {e}")


    def delete(self,endpoint):
        try:
            return self.session.delete(self.url+endpoint)
        except requests.exceptions.RequestException as e:
            raise Exception(f"DELETE request failed: {e}")