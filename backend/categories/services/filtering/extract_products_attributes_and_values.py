class ExtractProductsAttributesAndValues:
    def __init__(self, products):
        self.products = products

    def execute(self):
        products_attributes_and_values = {}

        for product in self.products:
            product_eavs = product.eavs.all().values_list("attribute__slug", "values__slug").distinct()

            for attribute, value in product_eavs:
                if attribute not in products_attributes_and_values.keys():
                    products_attributes_and_values[attribute] = [value]
                else:
                    if value not in products_attributes_and_values[attribute]:
                        products_attributes_and_values[attribute].append(value)

        return products_attributes_and_values
