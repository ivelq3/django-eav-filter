from os import name
from django.core.management.base import BaseCommand
from categories.services.csv_import import start_import


class Command(BaseCommand):
    help = "import products"

    def handle(self, *args, **options):
        start_import()
