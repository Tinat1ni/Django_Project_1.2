from .models import Category
from django.db.models import Count
from django.urls import resolve

def shop_context(request):
    top_level_categories = Category.objects.filter(parent__isnull=True)
    all_categories = Category.objects.annotate(product_count=Count('products'))
    view_name = resolve(request.path).url_name

    return {
        'top_level_categories': top_level_categories,
        'all_categories': all_categories,
        'view_name': view_name
    }