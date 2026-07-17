from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker

from shop.models import ProductCategory


class Command(BaseCommand):
    help = "Create 10 fake product categories"

    def handle(self, *args, **kwargs):
        fake = Faker()

        created = 0

        while created < 10:
            title = fake.unique.word().title()

            ProductCategory.objects.get_or_create(
                title=title,
                slug=slugify(title, allow_unicode=True),
            )

            created += 1

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {created} categories.")
        )