from categories.models import Category
from django.core.paginator import Paginator
from products.models import ProductAttribute
from products.serializers import FilterSetSerializer, ProductSerializer
from products.services.filtering.extract_filter_set import ExtractFilterSet
from products.services.filtering.extract_nested_filter_set import ExtractNestedFilterSet
from products.services.filtering.product_filter import ProductFilter


class CategoryDetailViewPresenter:

    PER_PAGE = 20
    ORDER_BY = "price"

    def __init__(self, request, category_slug):
        self.request = request
        self.filter_params = self.__filter_params()
        self.category = Category.objects.get(slug=category_slug)
        self.category_products = self.category.products.all()
        self.category_products_filter_set = self.__category_products_filter_set()
        self.filtered_products = self.__filtered_products()
        self.filtered_products_filter_set = self.__filtered_products_filter_set()

    def products(self):
        products = self.filtered_products.order_by(self.request.query_params.get("order_by", self.ORDER_BY))
        paginator = Paginator(products, self.PER_PAGE)
        page_obj = paginator.get_page(self.request.query_params.get("page", 1))
        return ProductSerializer(page_obj.object_list, many=True, context={"request": self.request}).data

    def products_count(self):
        return self.filtered_products.count()

    def filter_set(self):
        self.category_products_filter_set.disable_not_possible_filter_options(other_filter_set=self.filtered_products_filter_set)
        self.category_products_filter_set.sort_items()
        self.category_products_filter_set.sort_items_values()
        return FilterSetSerializer(self.category_products_filter_set).data

    def per_page(self):
        return self.PER_PAGE

    def category_name(self):
        return self.category.name

    def min_price(self):
        return self.category_products.order_by("price").first().price

    def max_price(self):
        return self.category_products.order_by("price").last().price

    def selected_min_and_max_price(self):
        selected_min_price = self.request.query_params.get("min_price")
        selected_max_price = self.request.query_params.get("max_price")

        if selected_min_price and selected_max_price:
            return [selected_min_price, selected_max_price]

        else:
            filtered_products_min_price = self.filtered_products.order_by("price").first().price
            filtered_products_max_price = self.filtered_products.order_by("price").last().price
            return [filtered_products_min_price, filtered_products_max_price]

    def selected_order_by(self):
        return self.request.query_params.get("order_by", self.ORDER_BY)

    def selected_filters(self):
        return self.filter_params

    def __category_products_filter_set(self):
        return ExtractFilterSet(products=self.category_products).execute()

    def __filtered_products(self):
        return ProductFilter(
            filter_params=self.filter_params,
            products=self.category_products,
            min_price=self.request.query_params.get("min_price"),
            max_price=self.request.query_params.get("max_price"),
        ).execute()

    def __filtered_products_filter_set(self):
        return ExtractNestedFilterSet(
            filter_params=self.filter_params,
            category_products=self.category_products,
            category_filter_set=self.category_products_filter_set,
            min_price=self.request.query_params.get("min_price"),
            max_price=self.request.query_params.get("max_price"),
        ).execute()

    def __filter_params(self):
        filter_params = {}

        allowed_params = ProductAttribute.objects.values_list("slug", flat=True).distinct()

        for param in allowed_params:
            if param in self.request.query_params:
                filter_params.update({param: self.request.query_params.getlist(param)})

        return filter_params
