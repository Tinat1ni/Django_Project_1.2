from django.shortcuts import render, get_object_or_404, redirect
# from django.views.decorators.vary import vary_on_cookie
from .models import Product, Category
from django.views.generic import View, ListView, DetailView, TemplateView
# from django.views.decorators.cache import cache_page
# from django.utils.decorators import method_decorator
from django.core.cache import cache
# from django.utils.cache import get_cache_key

class HomeView(TemplateView):          #for now
    template_name = 'index.html'

# @method_decorator(vary_on_cookie, name='dispatch')
# @method_decorator(cache_page(60 * 20), name='dispatch')
class ShopView(ListView):
    model = Product
    template_name = 'new_shop.html'
    context_object_name = 'products_list'
    paginate_by = 6

    def get_cache_key(self):
        cache_key = f"shop_products_{self.request.path}_{self.request.GET.urlencode()}"
        return cache_key

    def get_queryset(self):
        cache_key = self.get_cache_key()
        cached_products = cache.get(cache_key)

        if cached_products:
            return cached_products


        queryset = super().get_queryset()

        # search functionality
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(name__contains=search_query)

        # filtering by tags
        tag_filter = self.request.GET.get('category', None)
        if tag_filter == 'fresh':
            queryset = queryset.filter(fresh=True)
        elif tag_filter == 'discount':
            queryset = queryset.filter(discount=True)

        #sorting functionality based on dropdown selection
        sort_option = self.request.GET.get('fruitlist', None)
        if sort_option == 'price-':
            queryset = queryset.order_by('price')
        elif sort_option == 'price+':
            queryset = queryset.order_by('-price')
        elif sort_option == 'added+':
            queryset = queryset.order_by('-created_at')
        elif sort_option == 'added-':
            queryset = queryset.order_by('created_at')

        # filtering by price
        range_input = self.request.GET.get('rangeInput', None)
        if range_input:
            queryset = queryset.filter(price__lte=range_input)

        cached_products = list(queryset)
        cache.set(cache_key, cached_products, timeout=60 * 20)

        return queryset


class ProductDetail(DetailView):
    model = Product
    template_name = 'shop_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = self.object.name
        return context


class CategoryPageView(View):
    template_name = 'new_shop.html'

    def get(self, request, category_name):
        category = get_object_or_404(Category, name=category_name)
        products_list = Product.objects.filter(category=category)

        context = {
            'category': category,
            'products_list': products_list,
            'view_name': category_name,
            'search_query': request.GET.get('search', '')
        }
        return render(request, self.template_name, context)


def contact_view(request):
    return render(request, 'contact.html')