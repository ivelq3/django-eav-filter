import factory

from products.models import Eav, Product, ProductAttribute, ProductAttributeValue

factory.Faker._DEFAULT_LOCALE = "ru_RU"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        django_get_or_create = ("name",)

    name = factory.Faker("word")
    price = factory.Faker("pyint")

    @factory.post_generation
    def eavs(self, create, extracted):
        if not create:
            return
        if extracted:
            for eav in extracted:
                self.eavs.add(eav)


class ProductAttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductAttribute
        django_get_or_create = ("name",)

    name = factory.Faker("word")


class ProductAttributeValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductAttributeValue
        django_get_or_create = ("name",)

    name = factory.Faker("color")


class EavFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Eav

    attribute = factory.SubFactory(ProductAttributeFactory)
    values = factory.SubFactory(ProductAttributeValueFactory)

    @factory.post_generation
    def values(self, create, extracted):
        if not create:
            return
        if extracted:
            for value in extracted:
                self.values.add(value)
