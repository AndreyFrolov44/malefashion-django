from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description_lite = models.TextField()
    description = models.TextField()
    additional_information = models.TextField()
    quantity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=210)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.product


class ProductSize(models.Model):
    value = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.value


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


class RelatedProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    related = models.ForeignKey(Product, on_delete=models.CharField, related_name='related')

    def __str__(self):
        return self.product


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=210)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content_type
