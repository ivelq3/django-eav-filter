from rest_framework.views import APIView
from rest_framework.response import Response

from categories.models import Category
from categories.serializers import CategorySerializer
from categories.presenters.category_detail_view import CategoryDetailViewPresenter

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class CategoryDetailView(APIView):

    @method_decorator(cache_page(60*60*2))
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
        import json

        tree = json.dumps(self.flat_tree_to_dict(Category.objects.all(), 3), ensure_ascii=False, indent=4).encode("utf8")
        return Response(tree)

    def flat_tree_to_dict(self, nodes, max_depth):
        tree = []
        last_levels = [None] * max_depth
        for n in nodes:
            d = {"id": n.id, "name": n.name, "slug": n.slug}
            if n.level == 0:
                tree.append(d)
            else:
                parent_dict = last_levels[n.level - 1]
                if "children" not in parent_dict:
                    parent_dict["children"] = []
                parent_dict["children"].append(d)
            last_levels[n.level] = d
        return tree
