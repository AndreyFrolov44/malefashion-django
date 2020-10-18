from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('shop', views.ProductListView.as_view()),
    path('shop/<int:pk>', views.ProductDetailView.as_view()),
]