import json

from src.apis.orders_api import OrdersApi
import pytest
from src.utils import validators

from src.utils.logger import get_logger

logger = get_logger(__name__,"Order_flow_logs")

@pytest.fixture
def orders_api():
    return OrdersApi()

def test_get_all_orders(orders_api):
    res=orders_api.get_all_orders()
    order=res.json()
    assert res.status_code == 200,"Wrong status code"
    items=order.get("items")
    assert len(items)>0,"No items returned"
    logger.info("All orders fetched successfully")
    validators.validate_schema(order,'orders_schema.json')
    logger.info("Order Schema verified successfully")

def test_create_order(orders_api):
    res=orders_api.create_new_order()
    assert res.status_code==200,"Wrong status code"
    logger.info("Order created successfully")



def test_get_order_by_id(orders_api):
    res=orders_api.get_order_by_id(1)
    assert res.status_code==200,"Wrong status code"
    logger.info("Order by ID retrieved successfully")

def test_update_order_by_id(orders_api):
    res=orders_api.update_order_by_id(1)
    assert res.status_code == 200
    assert  res.json()['id']==1
    logger.info("Order by ID updated successfully")

def test_order_summary(orders_api):
    res=orders_api.get_order_summary()
    assert res.status_code==200,"Wrong status code"
    logger.info("Order summary retrieved successfully")

