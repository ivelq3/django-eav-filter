class ProductFilter:
    def __init__(self, selected_filters, products, skip_value):
        self.selected_filters = selected_filters
        self.products = products
        self.skip_value = skip_value

    def execute(self):
        for search_key, search_values_list in self.selected_filters.items():
            if search_key != self.skip_value and search_key != "page":
                self.products = self.products.filter(eavs__values__slug__in=search_values_list)

        return self.products.distinct()
