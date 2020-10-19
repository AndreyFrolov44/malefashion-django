from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('shop', views.ProductListView.as_view()),
    path('shop/<int:pk>', views.ProductDetailView.as_view()),
    path('shop/create', views.ProductCreateView.as_view()),

    path('category', views.CategoryView.as_view()),
    path('category/create', views.CategoryCreateView.as_view()),

    path('brands', views.BrandView.as_view()),
    path('brands/create', views.BrandCreateView.as_view()),

    path('size', views.ProductSizeListView.as_view()),
    path('size/create', views.ProductSizeCreateView.as_view()),

    path('tag', views.TagListView.as_view()),
    path('tag/create', views.TagCreateView.as_view()),

    path('article', views.ArticleListView.as_view()),
    path('article/create', views.ArticleCreateView.as_view()),
    path('article/<int:pk>', views.ArticleDetailView.as_view()),
]