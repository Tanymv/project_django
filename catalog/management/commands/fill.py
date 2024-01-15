from django.core.management import BaseCommand

from catalog.models import Product, Category



class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        category_list = [
            {"name": "Молочные продукты"},
            {"name": "Мясо"},
        ]
        category_for_create = []
        for item in category_list:
            category_for_create.append(
                Category.objects.create(**item)
            )

        products_list = [
            {"name": "Молоко", "price": "100", "category": category_for_create[0]},
            {"name": "Куриное филе", "price": "213", "category": category_for_create[1]},
            {"name": "Йогурт", "price": "36", "category": category_for_create[0]}
        ]

        products_for_create = []

        for item in products_list:
            products_for_create.append(
                Product(**item)
            )

        Product.objects.bulk_create(products_for_create)
