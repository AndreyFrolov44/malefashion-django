from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import *


class CommentInline(GenericTabularInline):
    model = Comment


class ImageInline(GenericTabularInline):
    model = ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'brand', 'quantity', 'available',)
    list_editable = ('price', 'category', 'brand', 'quantity', 'available',)
    fields = (
        'name',
        ('price', 'category', 'brand',),
        'description_lite',
        'description',
        'additional_information',
        ('quantity', 'available',),
        'slug',
    )
    inlines = [
        CommentInline,
        ImageInline,
    ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(Rating)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('ip', 'star', 'product',)


@admin.register(RelatedProduct)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('product', 'related',)


@admin.register(Article)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date',)
    inlines = [
        CommentInline,
    ]



