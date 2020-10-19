from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import (ProductListSerializer,
                          ProductDetailSerializer,
                          ProductCreateSerializer,
                          CategoryCreateSerializer,
                          CategorySerializer,
                          BrandCreateSerializer,
                          BrandSerializer,
                          ProductSizeListSerializer,
                          ProductSizeCreateSerializer,
                          TagListSerializer,
                          TagCreateSerializer, ArticleListSerializer, ArticleCreateSerializer)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductListSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductDetailSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer


class BrandView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandCreateView(generics.CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandCreateSerializer


class ProductSizeListView(generics.ListAPIView):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeListSerializer


class ProductSizeCreateView(generics.CreateAPIView):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeCreateSerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class TagCreateView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagCreateSerializer


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.filter(draft=False)
    serializer_class = ArticleListSerializer


class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(draft=False)
    serializer_class = ArticleCreateSerializer
