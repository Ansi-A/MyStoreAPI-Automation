import json

import pytest
from src.apis.products_api import ProductsApi
from src.utils.logger import get_logger

logger = get_logger(__name__,"ProductFlowLogs")
@pytest.fixture
def products_api():
    return ProductsApi()

def test_products_workflow(products_api):
    #create product
    res = products_api.create_product()
    product_id = res.json()['id']
    assert res.status_code == 201
    logger.info(f"Product created successfully")

    #get product by id
    res = products_api.get_product_by_id(product_id)
    assert res.status_code == 200
    assert res.json()['id'] == product_id
    logger.info(f"Product retrieved successfully: {res.json()}")

    #update product
    res = products_api.update_product(product_id)
    assert res.status_code == 200
    assert res.json()['id'] == product_id
    logger.info(f"Product updated successfully")

    #delete the product
    res = products_api.delete_product(product_id)
    assert res.status_code == 200
    assert "id" not in res.json(),"product not deleted"
    logger.info(f"Product deleted successfully")
