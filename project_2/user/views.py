from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import  login
from django.contrib import messages
from django.utils.translation import gettext as _

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('store:home')
        else:
            return render(request, 'registration.html', {'form': form})
    else:
        form = UserCreationForm()

    return render(request,'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('store:shop')
        else:
            messages.error(request, _('Username or password is incorrect'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


