import pytest

from src.apis.orders_api import OrdersApi
from src.utils.data_generator import OrderData


@pytest.fixture
def orders_api():
    return OrdersApi()

@pytest.mark.parametrize("payload,expected_status", [
    ({"shipping_address": None,"payment_method": None,"cart_id": None},422),
({"shipping_address": 123,"payment_method": 111,"cart_id": 111},422),
({"shipping_address": 'lahore',"payment_method": 'credit',"cart_id": 3},404),
({"shipping_address": "islamabad","payment_method": 333,"cart_id": 'jsj'},422),
({"shipping_address": 'lahore',"payment_method": 'debit',"cart_id": 5},404),


])
def test_create_order_negative(orders_api,payload,expected_status):
    res=orders_api.create_new_order_parameter_testing(payload)
    assert res.status_code == expected_status
