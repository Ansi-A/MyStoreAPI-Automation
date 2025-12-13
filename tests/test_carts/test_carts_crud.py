import pytest

from src.apis.carts_api import CartsApi
from src.utils import validators

from src.utils.logger import get_logger

logger = get_logger(__name__,"CartCrudLogs")
@pytest.fixture
def carts_api():
    return CartsApi()

def test_get_all_carts(carts_api):
    res = carts_api.get_all_carts()
    cart=  res.json()
    assert res is not None
    assert res.status_code == 200,"Wrong status code"
    logger.info("All Carts are fetched successfully")
    assert 'id' in cart[0], "ID not found in the first cart"

    validators.validate_schema(cart, 'cart_schema.json')
    logger.info("Carts Schema Validated")

def test_add_new_cart(carts_api):
    res = carts_api.create_new_cart()
    assert res.status_code == 200
    assert "id" in res.json(),"ID not found"
    logger.info("New Cart created successfully")

def test_get_cart_by_id(carts_api):
    res = carts_api.get_cart_by_id(5)
    assert res.status_code == 200
    assert "id" in res.json(), "ID not found"
    logger.info("Cart with id retrieved successfully")


def test_delete_cart_by_id(carts_api):
    res = carts_api.delete_cart_by_id(4)
    assert res.status_code == 200
    assert "id" not in res.json(), "Cart not deleted"
    logger.info("Cart with id deleted successfully")


def test_add_items_to_cart(carts_api):
    cart_res = carts_api.create_new_cart()
    assert cart_res.status_code == 200
    cart_id = cart_res.json()

    response = carts_api.add_items_to_cart(cart_id['id'])
    assert response.status_code == 200, "Product was not added to the cart"

    logger.info("Item added to cart successfully")






