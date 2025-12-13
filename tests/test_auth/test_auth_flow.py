import json

import pytest

from src.apis.auth_api import AuthApi
from src.apis.users_api import UsersApi
from src.utils.data_generator import UserData
from src.utils.logger import get_logger

logger = get_logger(__name__,"AuthFlowlogs")


@pytest.fixture
def authApi():
    return AuthApi()
@pytest.fixture
def userApi():
    return UsersApi()


def test_auth_flow(authApi, userApi):
    user = UserData.create_user()
    #create new user
    res=authApi.signup_flow(user)
    user_id=res.json()['id']

    user_credientials={
        "username":user.get('username'),
        "password":user.get('password')
    }
    assert res.status_code == 200
    logger.info("user created successfully")

    #login
    res=authApi.login_flow(user_credientials)
    assert res.status_code == 200
    logger.info("user login successfully")

    #get user_by_id
    res=userApi.get_user_by_id(user_id)
    assert res.status_code == 200
    logger.info("user fetched by successfully")

    #update user
    res=userApi.update_user(user_id)
    assert res.status_code == 200
    logger.info("user updated successfully")

    #delete_user
    res=userApi.delete_user(user_id)
    assert res.status_code == 200
    logger.info("user deleted successfully")


