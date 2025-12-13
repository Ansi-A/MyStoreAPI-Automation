import pytest

from src.apis.auth_api import AuthApi

from src.utils.logger import get_logger

logger = get_logger(__name__,"Loginlogs")


@pytest.fixture
def authApi():
    return AuthApi()

def test_login(authApi):
    res=authApi.login()
    assert res.status_code == 200
    logger.info(f"Logged in Successfully")
