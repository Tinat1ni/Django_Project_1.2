from django.db import models
from versatileimagefield.fields import VersatileImageField

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                                    related_name='children', blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = VersatileImageField(upload_to='product_images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    weight = models.FloatField(help_text='enter product weight in kg')
    country_of_origin = models.CharField(max_length=255)
    quality = models.CharField(max_length=30)
    product_check = models.CharField(max_length=30)
    min_weight = models.FloatField(help_text='minimum weight in kg')

    #organic = models.BooleanField(default=False)
    fresh = models.BooleanField(default=False)
    #sales = models.BooleanField(default=False)
    discount = models.BooleanField(default=False)
    #expired = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name