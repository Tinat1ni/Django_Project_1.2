from django.shortcuts import  redirect, get_object_or_404
from .models import Cart, CartItem
from store.models import Product


def add_to_cart(request, product_id):
    print(request.POST)
    referer_url = request.META.get('HTTP_REFERER', '')
    product = get_object_or_404(Product, id=product_id)
    cart = request.user.cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart,product=product,defaults={'quantity':1})
    if not created:
        cart_item.quantity += int(request.POST.get('quantity',1))
        cart_item.save()
    return redirect(referer_url)


