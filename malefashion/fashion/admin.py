from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import *


class CommentInline(GenericTabularInline):
    model = Comment


class ImageInline(GenericTabularInline):
    model = ProductImage


class ProductSizeQuantityInline(GenericTabularInline):
    model = ProductSizeQuantity


# class RelatedProductInline(GenericTabularInline):
#     model = RelatedProduct


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'sale', 'category', 'brand', 'available',)
    list_editable = ('price', 'sale', 'category', 'brand', 'available',)
    fields = (
        'name',
        ('price', 'sale', 'category', 'brand',),
        'description_lite',
        'description',
        'additional_information',
        'image',
        'tags',
        'related_products',
        'available',
        'slug',
    )
    inlines = [
        ImageInline,
        ProductSizeQuantityInline,
        # RelatedProductInline,
        CommentInline,
    ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('value',)
    prepopulated_fields = {'slug': ('value',)}


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(Rating)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('ip', 'star', 'product',)


@admin.register(Article)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date',)
    inlines = [
        CommentInline,
    ]



