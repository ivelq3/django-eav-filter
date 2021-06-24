import pytest

from tests.factories import EavFactory, ProductAttributeFactory, ProductAttributeValueFactory, ProductFactory


@pytest.fixture()
def create_product():
    def _create_product(product_name, eavs=None):
        if eavs:
            product_eavs = []
            for eav in eavs:
                for attribute_name, values_names in eav.items():
                    attribute = ProductAttributeFactory(name=attribute_name)
                    values = [ProductAttributeValueFactory(name=value_name) for value_name in values_names]
                    eav = EavFactory.create(attribute=attribute, values=(*values,))
                    product_eavs.append(eav)
            product = ProductFactory(name=product_name, eavs=(*product_eavs,))
            return product

        product = ProductFactory(name=product_name)
        return product

    return _create_product
