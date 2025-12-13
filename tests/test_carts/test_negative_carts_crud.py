import json


import pytest

from src.apis.carts_api import CartsApi


@pytest.fixture
def carts_api():
    return CartsApi()

@pytest.mark.parametrize("body,statuscode",[
({'status':"active","items":""},422),
({'status':"not-active","items":""},422),
({'status':"active","items":3},422),
({'status':"","items":88},422),
({"status": "active", "items": [{"product_id": 1, "quantity": 1}]}, 200),
])
def test_add_new_cart_negative(carts_api,body,statuscode):
    res = carts_api.create_new_cart_negative(body)
    print(json.dumps(res.json(), indent=4))
    assert res.status_code == statuscode









