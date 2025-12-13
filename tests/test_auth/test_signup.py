import pytest

from src.apis.auth_api import AuthApi
from src.utils.logger import get_logger

logger = get_logger(__name__,"signuplogs")


@pytest.fixture
def authApi():
    return AuthApi()

def test_signup(authApi):
     res=authApi.signup()
     assert res.status_code == 200
     logger.info(f"signup Completed ")

