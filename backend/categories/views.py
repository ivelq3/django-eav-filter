from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from products.serializers import FilterSetSerializer, ProductSerializer
from products.services.filtering.extract_filter_set import ExtractFilterSet
from products.services.filtering.extract_nested_filter_set import ExtractNestedFilterSet
from products.services.filtering.product_filter import ProductFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from categories.models import Category
from categories.serializers import CategorySerializer


# @method_decorator(cache_page(60 * 60), name="dispatch")
class CategoryDetailView(APIView):
    def get(self, request, slug):
        selected_filters = {k: v for k, v in request.query_params.lists()}
        category = Category.objects.get(slug=slug)
        base_products = category.products.all()
        base_products_filter_set = ExtractFilterSet(products=base_products).execute()

        filtered_products = ProductFilter(selected_filters=selected_filters, products=base_products, skip_value=None).execute()
        filtered_products_filter_set = ExtractNestedFilterSet(
            selected_filters=selected_filters,
            base_filter_set=base_products_filter_set,
            base_products=base_products,
        ).execute()

        base_products_filter_set.disable_not_possible_filter_options(other_filter_set=filtered_products_filter_set)

        product_serializer = ProductSerializer(filtered_products, many=True, context={"request": request})
        filter_set_serializer = FilterSetSerializer(base_products_filter_set)
        return Response(
            {
                "products": product_serializer.data,
                "filterSet": filter_set_serializer.data,
                "categoryName": category.name,
                "selectedFilters": selected_filters,
            }
        )


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return Response(category_serializer.data)
