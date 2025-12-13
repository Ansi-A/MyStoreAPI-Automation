import json

import pytest
from src.apis.products_api import ProductsApi
from src.utils import validators

@pytest.fixture
def products_api():
    return ProductsApi()


@pytest.mark.parametrize("endpoint,statuscode", [
    ({"page": 0}, 422),
    ({"limit": 0}, 422),
    ({"limit": 150}, 422),
    ({"min_price": 200, "max_price": 100}, 422),
    ({"min_price": "cheap"}, 422),
    ({"sort_by": "invalid_field"}, 422),
    ({"sort_order": "invalid"}, 422),
    ({"is_active": "not_bool"}, 422),
    ({"unknown_param": "test"}, 422),
    ({" "}, 422),
    ({56: "test"}, 422),

])
def test_get_all_products_negative(products_api, endpoint, statuscode):
    res = products_api.get_all_products_negative(endpoint)
    print(res.json())
    assert res.status_code == statuscode


@pytest.mark.parametrize("payload,statuscode",[
    ({}, 422),
    ({"name": "Test"}, 422),
    ({"name": 123, "price": 10, "category": "cat", "stock": 5}, 422),
    ({"name": "Test", "price": "free", "category": "cat", "stock": 5}, 422),
    ({"name": "Test", "price": 10, "category": "cat", "stock": "five"}, 422),
    ({"name": "Test", "price": 0, "category": "cat", "stock": 5}, 422),
    ({"name": "Test", "price": 10, "category": "cat", "stock": -1}, 422),
])
def test_create_new_product_negative(products_api,payload,statuscode):
    res = products_api.create_product_negative(payload)
    print(res.json())
    assert res.status_code == statuscode

