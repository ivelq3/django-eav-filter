from django.core.paginator import Paginator

from categories.models import Category
from products.models import ProductAttribute
from products.serializers import FilterSetSerializer, ProductSerializer
from products.services.filtering.extract_filter_set import ExtractFilterSet
from products.services.filtering.extract_nested_filter_set import ExtractNestedFilterSet
from products.services.filtering.product_filter import ProductFilter


class CategoryDetailViewPresenter:

    PER_PAGE = 20

    def __init__(self, request, category_slug):
        self.request = request
        self.page = self.request.query_params.get("page", 1)
        self.sort_by = self.request.query_params.get("sort_by")
        self.category = Category.objects.get(slug=category_slug)
        self.base_products = self.category.products.all()
        self.filter_params = self.__extract_filter_params()

    def products(self):
        filtered_products = ProductFilter(filter_params=self.filter_params, products=self.base_products, skip_value=None).execute()
        paginator = Paginator(filtered_products, self.PER_PAGE)
        page_obj = paginator.get_page(self.page)
        product_serializer = ProductSerializer(page_obj.object_list, many=True, context={"request": self.request})
        return product_serializer.data

    def filter_set(self):
        base_products_filter_set = ExtractFilterSet(products=self.base_products).execute()

        filtered_products_filter_set = ExtractNestedFilterSet(
            filter_params=self.filter_params,
            base_filter_set=base_products_filter_set,
            base_products=self.base_products,
        ).execute()

        base_products_filter_set.disable_not_possible_filter_options(other_filter_set=filtered_products_filter_set)
        base_products_filter_set.sort_items()
        base_products_filter_set.sort_items_values()
        filter_set_serializer = FilterSetSerializer(base_products_filter_set)
        return filter_set_serializer.data

    def category_name(self):
        return self.category.name

    def selected_filters(self):
        return self.filter_params

    def __extract_filter_params(self):
        filter_params = {}

        allowed_params = ProductAttribute.objects.values_list("slug", flat=True).distinct()

        for param in allowed_params:
            if param in self.request.query_params:
                filter_params.update({param: self.request.query_params.getlist(param)})

        return filter_params
