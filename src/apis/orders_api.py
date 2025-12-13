from src.client.base_api import BaseApi
from src.utils.conftest import Configuration
from src.utils.data_generator import OrderData



class OrdersApi(BaseApi):
    def get_all_orders(self):
        headers=self.admin_token('auth/login',Configuration.ADMIN_BODY)
        return self.get('orders/',headers=headers)

    def create_new_order(self):
        headers=self.admin_token('auth/login',Configuration.ADMIN_BODY)
        order=OrderData.create_order()
        return self.post('orders/',body=order,headers=headers)

    def get_order_by_id(self, order_id):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        return self.get(f'orders/{order_id}',headers=headers)

    def update_order_by_id(self, order_id):
        headers=self.admin_token('auth/login', Configuration.ADMIN_BODY)
        body=OrderData.update_order()
        return self.put(f'orders/{order_id}/status',body=body,headers=headers)

    def get_order_summary(self):
        headers=self.admin_token('auth/login', Configuration.ADMIN_BODY)
        return self.get('/orders/stats/summary',headers=headers)

    def create_order_from_given_cart(self,cart_id):
        headers=self.admin_token('auth/login', Configuration.ADMIN_BODY)
        order=OrderData.create_order_from_cart(cart_id)
        return self.post('/orders/',body=order,headers=headers)


    #functions for parameterize testing


    def create_new_order_parameter_testing(self,payload):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)

        return self.post('orders/', body=payload, headers=headers)

    def get_order_by_id(self, order_id):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        return self.get(f'orders/{order_id}', headers=headers)

    def update_order_by_id(self, order_id):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        body = OrderData.update_order()
        return self.put(f'orders/{order_id}/status', body=body, headers=headers)

    def get_order_summary(self):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        return self.get('/orders/stats/summary', headers=headers)

    def create_order_from_given_cart(self, cart_id):
        headers = self.admin_token('auth/login', Configuration.ADMIN_BODY)
        order = OrderData.create_order_from_cart(cart_id)
        return self.post('/orders/', body=order, headers=headers)
