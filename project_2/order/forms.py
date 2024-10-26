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
        product = cleaned_data.get('product')
        requested_quantity = cleaned_data.get('quantity')

        if product:
            if requested_quantity > product.quantity:
                raise ValidationError(f'only {product.quantity} products available for {product.name}')

        return cleaned_data


