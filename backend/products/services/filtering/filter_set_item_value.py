from dataclasses import dataclass

from products.models import ProductAttributeValue


@dataclass
class FilterSetItemValue:
    name: str
    slug: str
    disabled: bool = False

    def disable(self):
        self.disabled = True


class FilterSetItemValueBuilder:
    def __init__(self, product_attribute_values_slugs):
        self.product_attribute_values_slugs = product_attribute_values_slugs

    def execute(self):
        filter_set_item_values = []

        for slug in self.product_attribute_values_slugs:
            value_record = ProductAttributeValue.objects.get(slug=slug)
            filter_set_item_value = FilterSetItemValue(name=value_record.name.capitalize(), slug=value_record.slug)
            filter_set_item_values.append(filter_set_item_value)

        return filter_set_item_values
