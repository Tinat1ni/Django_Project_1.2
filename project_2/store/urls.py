from django.urls import path
from .views import HomeView, ShopView, CategoryPageView, ProductDetail, contact_view

app_name='store'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('category/<str:category_name>/', CategoryPageView.as_view(), name='category_page'),
    path('product/<int:id>/', ProductDetail.as_view(), name='product_detail'),
    path('contact', contact_view, name='contact')
]