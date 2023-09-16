# create_fake_date

import random
from django.core.management.base import BaseCommand
from home3.models import Client, Product, Order


class Command(BaseCommand):
    help = "Generate fake clients, products, orders."

    def _create_client(self, index: int):
        client = Client(name=f"client_{index}", email=f"client_{index}@email.com", tel="12345678901",
                        adress=f"address client_{index}")
        client.save()

    def _create_product(self, index: int) -> None:
        product = Product(name=f"product_{index}", description=f"description product_{index}",
                          price=1.00, count=random.randint(0, 10))
        product.save()

    def _create_orders(self, client: Client, count_products: int):
        count_client_products = random.randint(1, count_products)
        for i in range(count_client_products):
            product_id = random.randint(1, count_products)
            #product = Product.objects.get(id=product_id)
            order = Order(client=client)
            order.product.set(product_id)
            order.save()
        self._create_order_price(client)

    def _create_order_price(self, client: Client):
        orders = Order.objects.filter(client=client)
        common_price = 0
        for ord in orders:
            common_price += Product.objects.filter(id=ord.product_id).first()
        for ord in orders:
            ord.common_price = common_price
            ord.save()

    def add_arguments(self, parser):
        parser.add_argument('count_clients', type=int, help='count clients')
        parser.add_argument('count_products', type=int, help='count products')

    def handle(self, *args, **kwargs):

        count_clients = kwargs.get('count_clients')
        count_products = kwargs.get('count_products')

        # заполнение таблицы товаров
        print('заполнение таблицы товаров')
        #for j in range(count_products):
        #    self._create_product(j)

        # заполнение таблицы клиентов и заказов
        #for i in range(count_clients):
        #    self._create_client(i)  # заполнение таблицы клиентов

        # заполнение таблицы заказов
        for client in Client.objects.all():
            self._create_orders(client, count_products)  # заполение таблицы заказов

