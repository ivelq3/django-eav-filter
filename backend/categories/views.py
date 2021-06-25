from rest_framework.response import Response
from rest_framework.views import APIView


from categories.models import Category
from categories.presenters.category_detail_view import CategoryDetailViewPresenter
from categories.serializers import CategorySerializer


class CategoryDetailView(APIView):
    def get(self, request, slug):
        obj = CategoryDetailViewPresenter(request=request, category_slug=slug)

        return Response(
            {
                "products": obj.products(),
                "filterSet": obj.filter_set(),
                "categoryName": obj.category_name(),
                "selectedFilters": obj.selected_filters(),
            }
        )


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return Response(category_serializer.data)
