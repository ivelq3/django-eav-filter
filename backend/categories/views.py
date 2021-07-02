from rest_framework.views import APIView
from rest_framework.response import Response

from categories.models import Category
from categories.serializers import CategorySerializer
from categories.presenters.category_detail_view import CategoryDetailViewPresenter


class CategoryDetailView(APIView):
    def get(self, request, slug):

        obj = CategoryDetailViewPresenter(request=request, category_slug=slug)

        return Response(
            {
                "perPage": obj.per_page(),
                "products": obj.products(),
                "minPrice": obj.min_price(),
                "maxPrice": obj.max_price(),
                "filterSet": obj.filter_set(),
                "categoryName": obj.category_name(),
                "productsCount": obj.products_count(),
                "selectedFilters": obj.selected_filters(),
                "selectedOrderBy": obj.selected_order_by(),
                "selectedMinAndMaxPrice": obj.selected_min_and_max_price(),
            }
        )


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return Response(category_serializer.data)
