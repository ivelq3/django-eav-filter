from django.urls import path

from categories.views import CategoryDetailView, CategoryListView

urlpatterns = [
    path("categories/", CategoryListView.as_view()),
    path("categories/<slug:slug>", CategoryDetailView.as_view()),
]
