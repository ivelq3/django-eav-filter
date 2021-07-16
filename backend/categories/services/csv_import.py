import csv

from categories.models import Category
from products.models import Eav, Product, ProductAttribute, ProductAttributeValue


class CsvImport:
    def __init__(self, row):
        self.row = row

    def create_product(self):
        product_name = self.row.get("product")
        product_price = self.row.get("price")
        product, _ = Product.objects.get_or_create(name=product_name, price=int(product_price))
        product.eavs.clear()
        return product

    def create_category(self):
        root_category = self.row.get("root_category")
        sub_category = self.row.get("sub_category")
        sub_sub_category = self.row.get("sub_sub_category")

        if root_category:
            root_category, _ = Category.objects.get_or_create(name=root_category)

        if sub_category:
            sub_category, _ = Category.objects.get_or_create(name=sub_category, parent=root_category)

        if sub_sub_category:
            sub_sub_category, _ = Category.objects.get_or_create(name=sub_sub_category, parent=sub_category)

        if sub_sub_category:
            return sub_sub_category
        elif sub_category:
            return sub_category
        else:
            return root_category

    def create_attribute(self, attribute_name):
        attribute, _ = ProductAttribute.objects.get_or_create(name=attribute_name)
        return attribute

    def create_attribute_value(self, attribute_value_name):
        value, _ = ProductAttributeValue.objects.get_or_create(name=attribute_value_name)
        return value

    def create_eav(self, attribute, value):
        eav = Eav.objects.create(attribute=attribute)
        eav.values.add(value)
        eav.save()
        return eav

    def execute(self):
        print(self.row)
        product = self.create_product()
        category = self.create_category()
        product.category = category
        for attribute_name, attribute_value_name in self.row.items():
            if (
                attribute_name != "sub_sub_category"
                and attribute_name != "sub_category"
                and attribute_name != "root_category"
                and attribute_name != "product"
                and attribute_name != "price"
                and attribute_name != "category"
                and attribute_value_name != ""
            ):
                attribute = self.create_attribute(attribute_name)
                value = self.create_attribute_value(attribute_value_name)
                eav = self.create_eav(attribute, value)
                product.eavs.add(eav)
                product.save()


def start_import():
    csv_file = open("test_data/wallpapers.csv", "r")
    reader = csv.DictReader(csv_file, delimiter=";")

    for row in reader:
        CsvImport(row).execute()

    csv_file.close()
