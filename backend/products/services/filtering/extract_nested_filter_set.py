from products.services.filtering.extract_filter_set import ExtractFilterSetItem
from products.services.filtering.filter_set import FilterSet
from products.services.filtering.product_filter import ProductFilter


class ExtractNestedFilterSet:
    def __init__(self, filter_params, base_products, base_filter_set):
        self.filter_params = filter_params
        self.base_products = base_products
        self.base_filter_set = base_filter_set

    def execute(self):
        filter_set_items = []

        all_base_filter_set_attributes_slugs = self.base_filter_set.get_items_slugs()

        for attribute_slug in all_base_filter_set_attributes_slugs:
            filtered_products = ProductFilter(
                filter_params=self.filter_params,
                products=self.base_products,
                skip_value=attribute_slug,
            ).execute()
            # can return None if attribute slug not in filtered products
            # TODO make test
            filter_set_item = ExtractFilterSetItem(filtered_products, attribute_slug).execute()
            if filter_set_item:
                filter_set_items.append(filter_set_item)

        return FilterSet(items=filter_set_items)
