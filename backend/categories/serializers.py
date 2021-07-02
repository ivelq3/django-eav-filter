from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "slug")


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
