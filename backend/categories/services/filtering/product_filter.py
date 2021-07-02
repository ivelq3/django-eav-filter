class ProductFilter:
    def __init__(
        self,
        products,
        min_price,
        max_price,
        filter_params,
        skip_value=None,
    ):
        self.products = products
        self.min_price = min_price
        self.max_price = max_price
        self.skip_value = skip_value
        self.filter_params = filter_params

    def execute(self):

        if self.min_price and self.max_price:
            self.products = self.products.filter(price__range=(self.min_price, self.max_price))

        for search_key, search_values_list in self.filter_params.items():
            if search_key != self.skip_value:
                self.products = self.products.filter(eavs__values__slug__in=search_values_list)

        return self.products.distinct()
