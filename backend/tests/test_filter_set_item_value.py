import pytest
from slugify import slugify
from tests.factories import ProductAttributeValueFactory
from categories.services.filtering.filter_set_item_value import FilterSetItemValue, FilterSetItemValueBuilder


def test_filter_set_item_value_disable():
    value = FilterSetItemValue(name="white", slug="white")
    assert value.disabled == False
    value.disable()
    assert value.disabled == True


@pytest.mark.django_db
def test_filter_set_item_value_builder():
    value1 = ProductAttributeValueFactory(name="синий")
    value2 = ProductAttributeValueFactory(name="белый")

    product_attribute_values_slugs = [value1.slug, value2.slug]

    filter_set_item_values = FilterSetItemValueBuilder(product_attribute_values_slugs=product_attribute_values_slugs).execute()

    for value in filter_set_item_values:
        assert isinstance(value, FilterSetItemValue)
        assert value.name == value.name.capitalize()
        assert value.slug == slugify(value.name)
        assert value.disabled == False

    assert len(filter_set_item_values) == len(product_attribute_values_slugs)
