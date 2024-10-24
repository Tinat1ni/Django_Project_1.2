from django.urls import path
from .views import home, shop, product_detail, category_page

app_name='store'
urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('category/<str:category_name>/', category_page, name='category_page'),
    path('product/<int:id>/', product_detail, name='product_detail'),
]