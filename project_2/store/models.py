from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('სახელი'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                                    related_name='children', blank=True, null=True, verbose_name=_('მშობელი'))
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('სახელი'))
    description = models.TextField(blank=True, verbose_name=_('აღწერა'))
    price = models.FloatField(verbose_name=_('ფასი'))
    quantity = models.IntegerField(verbose_name=_('რაოდენობა'))
    image = VersatileImageField(upload_to='product_images/', null=True, blank=True, verbose_name=_('ფოტო'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name=_('კატეგორია'))
    weight = models.FloatField(help_text='enter product weight in kg', verbose_name=_('წონა'))
    country_of_origin = models.CharField(max_length=255)
    quality = models.CharField(max_length=30)
    product_check = models.CharField(max_length=30)
    min_weight = models.FloatField(help_text='minimum weight in kg')
    created_at = models.DateTimeField(auto_now_add=True)
    #organic = models.BooleanField(default=False)
    fresh = models.BooleanField(default=False)
    #sales = models.BooleanField(default=False)
    discount = models.BooleanField(default=False)
    #expired = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name