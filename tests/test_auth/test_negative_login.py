
import pytest

from src.apis.auth_api import AuthApi
from src.utils.conftest import Configuration


@pytest.fixture
def authApi():
    return AuthApi()

@pytest.mark.parametrize("body,response_code",[
({"username": 9854894,"password": 'jkdjd'},422),
    ({"username": 'salman',"password": ''},401),
({"username": 'salman',"password": "3434"},401),
({"username": '',"password": ""},401),
({"username": 'salman',"password": 84343},422),
({"username": 'salman',"password": "passcode"},200),
({"username": 'Jessica_Jimenez',"password": "password123"},200)

])
def test_negative_login(authApi,body,response_code):
    res=authApi.login_negative(body)
    print(res)
    assert res.status_code == response_code
