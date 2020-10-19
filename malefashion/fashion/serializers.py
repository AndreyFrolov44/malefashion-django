from rest_framework import serializers

from .models import Product, Comment, ProductSizeQuantity, ProductImage, Category, Brand, ProductSize, Tag, Article


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


class CommentListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('author', 'text', 'date',)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductSizeQuantitySerializer(serializers.ModelSerializer):
    size = serializers.SlugRelatedField(slug_field='value', read_only=True)

    class Meta:
        model = ProductSizeQuantity
        fields = ('size', 'quantity',)


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    brand = serializers.SlugRelatedField(slug_field='name', read_only=True)
    tags = TagSerializerField()
    related_products = ProductListSerializer(many=True)
    comments = CommentListSerializer(many=True)
    images = ProductImageSerializer(many=True)
    sizes = ProductSizeQuantitySerializer(many=True)

    class Meta:
        model = Product
        exclude = ('available',)


class ProductCreateSerializer(serializers.ModelSerializer):
    comments = CommentListSerializer(many=True)
    images = ProductImageSerializer(many=True)
    sizes = ProductSizeQuantitySerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSizeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'


class ProductSizeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('date', 'title', 'image_preview',)


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


# class ArticleDetailSerializer(serializers.ModelSerializer):
#     class Meta
#         model = Article
#         fields =

