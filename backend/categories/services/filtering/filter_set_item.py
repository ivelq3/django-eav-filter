from dataclasses import dataclass

from products.models import ProductAttribute
from categories.services.filtering.filter_set_item_value import FilterSetItemValueBuilder

# from django.core.cache import cache


@dataclass
class FilterSetItem:
    name: str
    slug: str
    values: list
    position: int = 100

    def __post_init__(self):
        if self.name == "Производитель":
            self.position = 0
        if self.name == "Коллекция":
            self.position = 1
        if self.name == "Цвет":
            self.position = 2


class FilterSetItemBuilder:
    def __init__(self, product_attribute_slug, product_attribute_values_slugs):
        self.product_attribute_slug = product_attribute_slug
        self.product_attribute_values_slugs = product_attribute_values_slugs

    def execute(self):
        
        # all_product_attributes = cache.get('all_product_attributes')
        
        # if all_product_attributes is None:
        #     all_product_attributes = ProductAttribute.objects.all()
        #     cache.set('all_product_attributes', all_product_attributes)

        # attribute_record = all_product_attributes.get(slug=self.product_attribute_slug)
        attribute_record = ProductAttribute.objects.get(slug=self.product_attribute_slug)

        filter_set_item_values = FilterSetItemValueBuilder(product_attribute_values_slugs=self.product_attribute_values_slugs).execute()
        return FilterSetItem(name=attribute_record.name.capitalize(), slug=attribute_record.slug, values=filter_set_item_values)
