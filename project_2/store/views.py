from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views.generic import View, ListView, DetailView, TemplateView


class HomeView(TemplateView):          #for now
    template_name = 'index.html'


class ShopView(ListView):
    model = Product
    template_name = 'new_shop.html'
    context_object_name = 'products_list'
    paginate_by = 6

    def get_queryset(self):
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







