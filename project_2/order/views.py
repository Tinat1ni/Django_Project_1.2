from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import FormView
from django.views.generic import DetailView
from .models import CartItem, Cart
from store.models import Product
from .forms import CartItemForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache

@method_decorator(never_cache, name='dispatch')
@method_decorator(login_required(login_url=reverse_lazy('user:login')), name='dispatch')
class AddToCartView(FormView):
    form_class = CartItemForm
    template_name = 'new_shop.html'

    def form_valid(self, form):
        product = form.cleaned_data['product']
        quantity = form.cleaned_data['quantity']

        cart = self.request.user.cart
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity':quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        referer_url = self.request.META.get('HTTP_REFERER', '')
        return redirect(referer_url)


@method_decorator(login_required(login_url=reverse_lazy('user:login')), name='dispatch')
class CartView(DetailView):
    model = Cart
    template_name = 'cart.html'
    context_object_name = 'cart'
    form_class = CartItemForm

    def get_object(self):
        return get_object_or_404(Cart, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = self.object.items.select_related('product')
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        for item in cart_items:
            item.total_price = item.product.price * item.quantity

        context['cart_items'] = cart_items
        context['total_price'] = total_price
        context['view_name'] = 'კალათა' # some_contexts.py ფაილშია განსაზღრვული view_name როგორც urlის სახელი და ამიტომ ვამატებ აქ
        return context

    def post(self, request, *args, **kwargs):
        if 'remove_item' in request.POST:
            item_id = request.POST.get('remove_item')
            CartItem.objects.filter(id=item_id, cart=self.get_object()).delete()
            return redirect(self.request.META.get('HTTP_REFERER', ''))
        return super().post(request, *args, **kwargs)



