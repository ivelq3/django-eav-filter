from categories.services.filtering.extract_filter_set import ExtractFilterSetItem
from categories.services.filtering.filter_set import FilterSet
from categories.services.filtering.product_filter import ProductFilter


class ExtractNestedFilterSet:
    def __init__(self, filter_params, category_products, category_filter_set, min_price, max_price):
        self.min_price = min_price
        self.max_price = max_price
        self.filter_params = filter_params
        self.category_products = category_products
        self.category_filter_set = category_filter_set

    def execute(self):
        filter_set_items = []

        all_category_filter_set_attributes_slugs = self.category_filter_set.get_items_slugs()

        for attribute_slug in all_category_filter_set_attributes_slugs:
            filtered_products = ProductFilter(
                filter_params=self.filter_params,
                products=self.category_products,
                skip_value=attribute_slug,
                min_price=self.min_price,
                max_price=self.max_price,
            ).execute()
            # can return None if attribute slug not in filtered products
            # TODO make test
            filter_set_item = ExtractFilterSetItem(filtered_products, attribute_slug).execute()
            if filter_set_item:
                filter_set_items.append(filter_set_item)

        return FilterSet(items=filter_set_items)
