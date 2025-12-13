from random import Random

import faker
import random



fake = faker.Faker()

class ProductData:
    @staticmethod
    def create_product():
        return {
            'name': fake.name(),
            'title': fake.text(max_nb_chars=8),
            'description': fake.paragraph(nb_sentences=2),
            'price': fake.pyint(min_value=1, max_value=100),
            'category': random.choice(["Men's Wear", "Baby Wear", "Accessories", 'Smart Technologies']),
            'image': fake.image_url(),
            'stock': random.randint(1, 99999),
        }

    @staticmethod
    def update_product():
        product_data = ProductData.create_product()

        product_data['name'] = fake.name()
        product_data['price'] = fake.pyint(min_value=1, max_value=100)
        return product_data

    @staticmethod
    def get_all_products_id_and_update_qty_if_needed():
        from src.apis.products_api import ProductsApi
        api = ProductsApi()
        res = api.get_all_products()
        items = res.json()['items']
        products_id = []
        for item in items:
            products_id.append(item['id'])
        for item in items:
            if item['stock'] == 0:
                p_id = item['id']
                product_stock = {'stock': 100}
                api.update_product_stock_only(p_id, product_stock)
        return products_id


class CartsData:

    @staticmethod
    def create_cart():
        product_ids = ProductData.get_all_products_id_and_update_qty_if_needed()
        chosen_product_id = random.choice(product_ids)

        return {
            "status": "active",
            "items": [
                {
                    "product_id": chosen_product_id,
                    "quantity": 1
                }
            ]
        }



    @staticmethod
    def create_cart_e2e(p_id):
        return {
            "status": "active",
            "items": [
                {
                    "product_id": p_id,
                    "quantity":1,
                }
            ]
        }
    @staticmethod
    def add_product_to_cart():

        all_ids = ProductData.get_all_products_id_and_update_qty_if_needed()
        product_id = random.choice(all_ids)

        return {
            "product_id": product_id,
            "quantity": 1
        }
    @staticmethod
    def e2e_add_product_to_cart(product_id):

        return{
      "product_id": product_id,
      "quantity": 1
    }


class OrderData:

    @staticmethod
    def create_order():
        from src.apis.carts_api import CartsApi
        api = CartsApi()

        cart_res = api.create_new_cart()
        cart_id = cart_res.json()["id"]

        return {
            "shipping_address": fake.address(),
            "payment_method": "COD",
            "cart_id": cart_id,
        }

    @staticmethod
    def create_order_from_cart(cart_id):
        return {

            "shipping_address": fake.address(),
            "payment_method": random.choice(["credit card", "debit card", "paypal", "COD"]),
            "cart_id": cart_id

        }
    @staticmethod
    def update_order():



        return {
            'status': random.choice(["pending", "delivered", "in shipment"]),
            'shipping_address': fake.address(),

        }

class UserData:

    @staticmethod
    def create_user():
        username = fake.name().replace(" ", "_")
        return {
            "username": username,
            "email": f'{username}@gmail.com',
            "role": "customer",
            "password": "password123",
        }

    @staticmethod
    def update_user():
        return {
          "username": fake.name(),
          "email": fake.email(),
          "password": "password123",
        }
