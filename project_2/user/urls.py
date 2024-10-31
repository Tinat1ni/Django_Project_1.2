from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import login_view, register

app_name = 'user'
urlpatterns = [
    path('register/', register, name='registration' ),
    path('', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='store:shop'), name = 'logout'),
]