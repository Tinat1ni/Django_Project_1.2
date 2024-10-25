from django import forms
from django.core.exceptions import ValidationError
from store.models import Product
from .models import CartItem

class CartItemForm(forms.ModelForm):

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

    def clean(self):
        cleaned_data = super().clean()
        product_id = cleaned_data.get('product')
        requested_quantity = cleaned_data.get('quantity')

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError(' selected product does not exist.')

        if requested_quantity and product:
            if requested_quantity > product.quantity:
                raise ValidationError(f'Only {product.quantity} units available.')

        return cleaned_data


