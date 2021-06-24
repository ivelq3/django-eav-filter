from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product
from products.serializers import ProductSerializer


class ProductDetailView(APIView):
    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        product_serializer = ProductSerializer(product)
        return Response(product_serializer.data)
