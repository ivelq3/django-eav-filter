import pytest
from slugify import slugify
from categories.models import Category

@pytest.mark.django_db
def test_auto_sluglify_product_name(create_product):
    product = create_product(product_name="товар")
    assert slugify(product.name) == product.slug
