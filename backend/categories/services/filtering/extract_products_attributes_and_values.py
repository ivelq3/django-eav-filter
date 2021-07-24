from products.models import Eav


class ExtractProductsAttributesAndValues:
    def __init__(self, products):
        self.products = products

    def execute(self):
        products_attributes_and_values = {}

        products_eav_ids = self.products.values_list('eavs', flat=True).distinct()
        eavs = Eav.objects.filter(id__in=products_eav_ids)
        attributes_and_values_slugs = eavs.values_list("attribute__slug", "values__slug").distinct()

        # for product in self.products:
        #     product_eavs = product.eavs.all().values_list("attribute__slug", "values__slug").distinct()

        for attribute, value in attributes_and_values_slugs:
            if attribute not in products_attributes_and_values.keys():
                products_attributes_and_values[attribute] = [value]
            else:
                if value not in products_attributes_and_values[attribute]:
                    products_attributes_and_values[attribute].append(value)

        return products_attributes_and_values
