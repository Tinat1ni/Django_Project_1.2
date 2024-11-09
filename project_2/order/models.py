from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart', verbose_name=_('მომხმარებელი'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('შექმნის დრო'))


class CartItem(models.Model):

    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items', verbose_name=_('კალათა'))
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE, verbose_name=_('პროდუქტი'))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_('რაოდენობა'))
    added_at = models.DateTimeField(auto_now_add=True)


    # @property
    # def total(self):
    #     return self.quantity * (self.product.price or 0)

    def __str__(self):
        return f'cart of {self.cart.user.username}'


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cart', 'product'], name='unique_cart_product')
        ]
