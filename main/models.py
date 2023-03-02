from django.db import models


class Manufacturer(models.Model):
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class Category(models.Model):
    title = models.CharField(max_length=100)


class Product(models.Model):
    title = models.CharField(max_length=100)
    size = models.IntegerField()
    price = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

