import pytest
from slugify import slugify
from tests.factories import ProductAttributeFactory, ProductAttributeValueFactory
from categories.services.filtering.filter_set_item import FilterSetItem, FilterSetItemBuilder
from categories.services.filtering.filter_set_item_value import FilterSetItemValue


@pytest.mark.parametrize("name, expected", [("Производитель", 0), ("Коллекция", 1), ("Цвет", 2), ("Размер", 100)])
def test_filter_set_item_position(name, expected):
    item = FilterSetItem(name=name, slug="slug", values=[])
    assert item.position == expected


@pytest.mark.django_db
def test_filter_set_item_builder():
    attribute = ProductAttributeFactory(name="цвет")
    attribute_value1 = ProductAttributeValueFactory(name="синий")
    attribute_value2 = ProductAttributeValueFactory(name="белый")
    product_attribute_values_slugs = [attribute_value1.slug, attribute_value2.slug]

    filter_set_item = FilterSetItemBuilder(
        product_attribute_slug=attribute.slug, product_attribute_values_slugs=product_attribute_values_slugs
    ).execute()

    assert filter_set_item.name == attribute.name.capitalize()
    assert filter_set_item.slug == slugify(attribute.name)
    for value in filter_set_item.values:
        assert isinstance(value, FilterSetItemValue)
