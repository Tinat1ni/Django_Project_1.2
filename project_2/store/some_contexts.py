from .models import Category
from django.db.models import Count
from django.urls import resolve
from order.models import CartItem


def shop_context(request):
    top_level_categories = Category.objects.filter(parent__isnull=True)
    all_categories = Category.objects.annotate(product_count=Count('products'))
    view_name = resolve(request.path).url_name
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart__user=request.user)
        cart_count = sum(item.quantity for item in cart_items)
    else:
        cart_count = 0
    return {
        'top_level_categories': top_level_categories,
        'all_categories': all_categories,
        'view_name': view_name,
        'cart_count': cart_count,
    }