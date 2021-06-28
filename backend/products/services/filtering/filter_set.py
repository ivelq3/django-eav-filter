from dataclasses import dataclass

from products.services.filtering.filter_set_item import FilterSetItemBuilder


@dataclass
class FilterSet:
    items: list

    def sort_items(self):
        self.items = sorted(self.items, key=lambda item: item.position)

    def sort_items_values(self):
        for item in self.items:
            item.values = sorted(item.values, key=lambda value: value.name)

    def get_items_slugs(self):
        slugs = set()

        for item in self.items:
            slugs.add(item.slug)

        return slugs

    def get_item_by_slug(self, slug):
        for item in self.items:
            if item.slug == slug:
                return item

    def get_items_values_names(self):
        names = set()

        for item in self.items:
            for value in item.values:
                names.add(value.name)

        return names

    def disable_not_possible_filter_options(self, other_filter_set):
        names_to_disable = self.get_items_values_names().difference(other_filter_set.get_items_values_names())

        for item in self.items:
            for value in item.values:
                if value.name in names_to_disable:
                    value.disable()

        return self


class FilterSetBuilder:
    def __init__(self, products_attributes_and_values):
        self.products_attributes_and_values = products_attributes_and_values

    def execute(self):
        filter_set_items = []

        for product_attribute_slug, product_attribute_values_slugs in self.products_attributes_and_values.items():
            filter_set_item = FilterSetItemBuilder(product_attribute_slug, product_attribute_values_slugs).execute()
            filter_set_items.append(filter_set_item)

        return FilterSet(items=filter_set_items)
