class ProductFilter:
    def __init__(self, filter_params, products, skip_value):
        self.filter_params = filter_params
        self.products = products
        self.skip_value = skip_value

    def execute(self):
        for search_key, search_values_list in self.filter_params.items():
            if search_key != self.skip_value:
                self.products = self.products.filter(eavs__values__slug__in=search_values_list)

        return self.products.distinct()
