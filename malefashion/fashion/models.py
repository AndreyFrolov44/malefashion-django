from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.content_type)


class ProductImage(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return '{}'.format(self.content_type)


class ProductSize(models.Model):
    value = models.CharField(max_length=3, unique=True)
    slug = models.SlugField(max_length=6, unique=True)

    def __str__(self):
        return self.value


class ProductSizeQuantity(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.content_type)


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    sale = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description_lite = models.TextField()
    description = models.TextField()
    additional_information = models.TextField()
    image = models.ImageField(upload_to='product')
    tags = models.ManyToManyField('Tag', blank=True, related_name='products')
    available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=210, unique=True)
    related_products = models.ManyToManyField('self', blank=True, related_name='related_products')
    comments = GenericRelation(Comment)
    images = GenericRelation(ProductImage)
    sizes = GenericRelation(ProductSizeQuantity)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class RatingStar(models.Model):
    value = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.value


class Rating(models.Model):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CharField)

    def __str__(self):
        return self.product


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image_preview = models.ImageField(upload_to='article', blank=True, null=True)
    image_detail = models.ImageField(upload_to='article', blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=210, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title




