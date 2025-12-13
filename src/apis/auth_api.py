from src.client.base_api import BaseApi
from src.utils.conftest import Configuration
from src.utils.data_generator import UserData

class AuthApi(BaseApi):
    def signup(self):
        body=UserData.create_user()

        return self.post('/auth/signup',body)

    def login(self):
        body=Configuration.USER_BODY
        return self.post('/auth/login',body)

    # def functions for flow
    def signup_flow(self,body):
        return self.post('/auth/signup', body)

    def login_flow(self,body):
        return self.post('/auth/login',body)

    #functions for edge and negative tests
    def signup_negative(self, body):
        return self.post('/auth/signup', body)
    def login_negative(self,body):
        return self.post('/auth/login',body)
