from django.core.management import BaseCommand
from catalog.models import Category, Product
import json
import os

ROOT_DIR = os.path.dirname(__file__)
# catalog.json
file_path = os.path.join(ROOT_DIR, 'catalog.json')


class Command(BaseCommand):

    @staticmethod
    def json_categories() -> list:
        """
        Получение данных из фикстуры с категориями
        :return: список с категориями
        """
        with open(file_path, encoding="utf-8") as file:
            values = json.load(file)
            print("value['model'] == catalog.category", values, end="\\")
        categories = [value for value in values if value['model'] == "catalog.category"]
        return categories

    @staticmethod
    def json_products() -> list:
        """
        Получение данных из фикстуры с продуктами
        :return: список с продуктами
        """
        with open(file_path, encoding="utf-8") as file:
            values = json.load(file)
            print("value['model'] == catalog.product", values, end="\\")
        products = [value for value in values if value['model'] == "catalog.product"]
        return products

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_for_create = []
        products_for_create = []

        for category in Command.json_categories():
            category_for_create.append(Category(**category))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_products():
            products_for_create.append(Product(**product))

        Product.objects.bulk_create(products_for_create)

