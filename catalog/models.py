from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=100)
    slug = models.SlugField(max_length=60)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
