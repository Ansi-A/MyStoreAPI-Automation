from src.utils.data_generator import ProductData
from src.utils.conftest import Configuration

from src.client.base_api import BaseApi

class ProductsApi(BaseApi):

    def get_all_products(self):
        return self.get('products/')

    def get_product_by_id(self, product_id):
        return self.get(f'products/{product_id}')

    def create_product(self):

        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        product=ProductData.create_product()
        return self.post(f'products', product, headers=headers)

    def update_product(self, product_id):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        product=ProductData.update_product()
        return self.put(f'products/{product_id}',product,headers=headers)

    def delete_product(self, product_id):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        return self.delete(f'products/{product_id}')

    #functions for negative and edge cases
    def get_all_products_negative(self,arguments):
        return self.get(f'products/{arguments}/')

    def create_product_negative(self,body):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        return self.post(f'products/', body=body,headers=headers)


    def update_product_stock_only(self,product_id,product):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)

        return self.put(f'products/{product_id}/',product,headers=headers)


