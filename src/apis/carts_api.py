import random

from src.client.base_api import BaseApi
from src.utils.conftest import Configuration
from src.utils.data_generator import CartsData,ProductData




class CartsApi(BaseApi):
    def get_all_carts(self):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        return self.get('carts/',headers=headers)


    def create_new_cart(self):
        cart_data = CartsData().create_cart()
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        return self.post('carts/',body=cart_data,headers=headers)

    def get_cart_by_id(self, cart_id):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        return self.get(f'carts/{cart_id}',headers=headers)

    def delete_cart_by_id(self, cart_id):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        return self.delete(f'carts/{cart_id}',headers=headers)

    def add_items_to_cart(self, cart_id):
        product = CartsData.add_product_to_cart()
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        return self.post(f'carts/{cart_id}/items',body=product,headers=headers)

    def add_product_to_cart(self, product,cart_id):

        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        return self.post(f'carts/{cart_id}/items',body=product,headers=headers)

    def create_cart(self,data):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)

        return self.post(f'carts/',body=data,headers=headers)

    #functions for negative tests
    def create_new_cart_negative(self,data):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        return self.post(f'carts/',body=data,headers=headers)