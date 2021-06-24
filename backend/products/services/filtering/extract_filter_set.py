from products.services.filtering.extract_products_attributes_and_values import ExtractProductsAttributesAndValues
from products.services.filtering.filter_set import FilterSetBuilder
from products.services.filtering.filter_set_item import FilterSetItemBuilder


class ExtractFilterSet:
    def __init__(self, products):
        self.products = products

    def execute(self):
        products_attributes_and_values = ExtractProductsAttributesAndValues(self.products).execute()
        return FilterSetBuilder(products_attributes_and_values).execute()


class ExtractFilterSetItem:
    def __init__(self, products, attribute_slug):
        self.products = products
        self.attribute_slug = attribute_slug

    def execute(self):
        products_attributes_and_values = ExtractProductsAttributesAndValues(self.products).execute()
        product_attribute_values_slugs = products_attributes_and_values.get(self.attribute_slug)

        if product_attribute_values_slugs:
            return FilterSetItemBuilder(
                product_attribute_slug=self.attribute_slug,
                product_attribute_values_slugs=product_attribute_values_slugs,
            ).execute()
