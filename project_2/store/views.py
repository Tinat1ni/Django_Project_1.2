from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    return render(request, 'index.html')

def shop(request):
    products_list = Product.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        products_list = Product.objects.filter(name__icontains=search_query)

    tag_filter = request.GET.get('category', None)
    if tag_filter == 'fresh':
        products_list = products_list.filter(fresh=True)
    elif tag_filter == 'discount':
        products_list = products_list.filter(discount=True)

    cart_item_count = request.user.cart.items.count()
    context = {
        'products_list': products_list,
        'search_query': search_query,
        'cart_item_count': cart_item_count
    }
    return render(request, 'new_shop.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})


def category_page(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    products_list = Product.objects.filter(category=category)
    context={
            'category': category,
            'products_list': products_list,
            'view_name': category_name
    }
    return render(request, 'new_shop.html', context)

def filter_by_price(request):
    if request.method == 'POST':
        max_price = request.POST.get('rangeInput')

    products = Product.objects.filter(price__lte=max_price)


    return render(request, 'new_shop.html', {'products': products})

