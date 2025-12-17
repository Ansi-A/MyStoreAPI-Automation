import json

import pytest
from src.apis.products_api import ProductsApi
from src.utils import validators
from src.utils.logger import get_logger

logger = get_logger(__name__,"ProductCrudLogs")

@pytest.fixture
def products_api():
    return ProductsApi()

def test_get_all_products(products_api):
    res = products_api.get_all_products()
    product=res.json()
    assert res.status_code == 200,"Wrong status code"
    assert res is not None
    logger.info("Products retrieved successfully")
    validators.validate_schema(product, 'products_schema.json')
    logger.info(f"Product Schema verified successfully")

def test_get_product_by_id(products_api):
    res = products_api.get_product_by_id(43)
    assert res.status_code == 200,"Wrong status code"
    assert res is not None
    logger.info("Product by ID retrieved successfully")

def test_create_new_product(products_api):
    res = products_api.create_product()
    assert res is not None
    assert res.status_code == 201
    logger.info("Product created successfully")

def test_update_product(products_api):
    res = products_api.update_product(6)
    assert res is not None
    assert res.status_code == 200, "Wrong status code"
    logger.info(f"Product updated successfully")

def test_delete_product(products_api):
    res = products_api.delete_product(6)
    assert res.status_code == 200, "Wrong status code"
    assert "id" not in res.json()
    logger.info(f"Product deleted successfully")
