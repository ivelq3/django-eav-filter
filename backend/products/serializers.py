from rest_framework import serializers

from products.models import Eav, Product, ProductAttribute, ProductAttributeValue


class FilterSetItemValueSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    slug = serializers.CharField(max_length=200)
    disabled = serializers.BooleanField(default=False)


class FilterSetItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    slug = serializers.CharField(max_length=200)
    values = FilterSetItemValueSerializer(many=True)


class FilterSetSerializer(serializers.Serializer):
    items = FilterSetItemSerializer(many=True)


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = ("id", "slug", "name")


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        fields = ("id", "slug", "name")


class EavSerializer(serializers.Serializer):
    attribute = ProductAttributeSerializer()
    values = ProductAttributeValueSerializer(many=True)

    class Meta:
        model = Eav
        fields = ("id", "attribute", "values")


class ProductSerializer(serializers.ModelSerializer):
    eavs = EavSerializer(many=True)
    main_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("id", "slug", "name", "price", "main_image", "eavs", "category")

    def get_main_image(self, product):
        if product.main_image:
            return self.context["request"].build_absolute_uri(product.main_image.url)
        else:
            return None
