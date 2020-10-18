from rest_framework import serializers

from .models import Product


class TagSerializerField(serializers.ListField):
    def to_representation(self, data):
        return data.values_list('name', flat=True)


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    brand = serializers.SlugRelatedField(slug_field='name', read_only=True)
    tags = TagSerializerField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'sale', 'category', 'brand', 'image', 'tags',)


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    brand = serializers.SlugRelatedField(slug_field='name', read_only=True)
    tags = TagSerializerField()
    related_products = ProductListSerializer(many=True)

    class Meta:
        model = Product
        exclude = ('available',)




