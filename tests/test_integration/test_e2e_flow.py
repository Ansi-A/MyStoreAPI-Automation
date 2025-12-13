import pytest
import json
from src.apis.users_api import UsersApi
from src.apis.auth_api import AuthApi
from src.apis.carts_api import CartsApi
from src.apis.orders_api import OrdersApi
from src.apis.products_api import ProductsApi
from src.utils.data_generator import UserData,CartsData
from src.utils.logger import get_logger

logger = get_logger(__name__,"e2e_Flowlogs")


@pytest.fixture
def userApi():
    return UsersApi()
@pytest.fixture
def authApi():
    return AuthApi()
@pytest.fixture
def cartApi():
    return CartsApi()
@pytest.fixture
def ordersApi():
    return OrdersApi()
@pytest.fixture
def productsApi():
    return ProductsApi()

def test_e2e_workflow(userApi, authApi, cartApi, ordersApi, productsApi):
    user = UserData.create_user()

    # create new user
    res = authApi.signup_flow(user)
    user_id = res.json()['id']

    user_credientials = {
        "username": user.get('username'),
        "password": user.get('password')
    }
    assert res.status_code == 200
    logger.info("User Created Successfully")


    # login
    res = authApi.login_flow(user_credientials)
    assert res.status_code == 200
    logger.info("User Logged in Successfully")

    #create a product
    product=productsApi.create_product()
    p_id=product.json()['id']
    logger.info("Product Created Successfully")

    #Create a cart
    data=CartsData.create_cart_e2e(p_id)
    cart=cartApi.create_cart(data)
    c_id = cart.json()['id']
    logger.info(f"Cart Created Successfully")


    #Add product to cart
    payload=CartsData.e2e_add_product_to_cart(p_id)
    add_product=cartApi.add_product_to_cart(payload,c_id)
    logger.info(f"Product add to Cart Successfully")




    #Create an order from that cart
    order=ordersApi.create_order_from_given_cart(c_id)
    o_id=order.json()['id']
    assert res.status_code == 200,"wrong status code"
    logger.info(f"Order Created Successfully")


    #Verify the order details
    order=ordersApi.get_order_by_id(o_id)
    assert order.status_code == 200,"wrong status code"
    logger.info(f"Order details fetched successfully")




