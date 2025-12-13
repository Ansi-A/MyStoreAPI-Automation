import pytest

from src.apis.auth_api import AuthApi
from src.utils.data_generator import fake


@pytest.fixture
def authApi():
    return AuthApi()

@pytest.mark.parametrize("body,response_code",[
({"username": 9854894,"email": "kdjfkjdjdj","role": "customer","password": 'jkdjd'},422),
({"username": 'salman',"email": "kdjfkjdjdj","role": "customer","password": ''},422),
({"username": 'salman',"email": "kdjfkjdjdj","role": "customer","password": "3434"},422),
({"username": '',"email": "kdjfkjdjdj","role": "customer","password": ""},422),
({"username": 'salman',"email": "kdjfkjdjdj","role": "student","password": "3434"},422),
({"username": 'asad',"email": "kdjfkjdjdj@gmail.com","role": "customer","password": "passcode"},400),
({"username": 'salman',"email": "kdjfkjdjdj@gmail.com","role": "customer","password": "passwork"},400),
({"username": 'Jessica_Jimenez',"email": "Jessica_Jimenez@gmail.com","role": "customer","password": "password123"},400),
({"username": 'Jessica_Jimenez',"email": "Jessica_Jimenez@gmail.com","role": "customer","password": 843843},422),
({"username": fake.first_name(),"email": fake.email(),"role": "customer","password": "password123"},200)

])
def test_negative_signup(authApi,body,response_code):
    res=authApi.signup_negative(body)
    print(res)
    assert res.status_code == response_code