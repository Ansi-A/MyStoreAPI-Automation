import json

import pytest

from src.apis.users_api import UsersApi
from src.utils import validators
from src.utils.logger import get_logger

logger = get_logger(__name__,"UserCrudLogs")

@pytest.fixture
def userApi():
    return UsersApi()


def test_get_user(userApi):
    user = userApi.get_users()
    u=user.json()
    assert user.status_code == 200

    logger.info(f"All Users successfully fetched")
    validators.validate_schema(u,'user_schema.json')
    logger.info(f"User Schema successfully validated")


def test_get_user_by_id(userApi):
    user = userApi.get_user_by_id(1)
    logger.info(f"User successfully fetched")

def test_update_user(userApi):
    user = userApi.update_user(1)

    u=user.json()
    assert u['email'] != 'salman@gmail.com'
    assert user.status_code == 200

    logger.info(f"User successfully updated")
