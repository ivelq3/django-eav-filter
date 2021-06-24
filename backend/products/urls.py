from django.urls import path

from products.views import ProductDetailView

urlpatterns = [
    path("products/<slug:slug>", ProductDetailView.as_view()),
]
