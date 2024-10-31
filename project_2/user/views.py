from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('store:shop')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})


    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('store:home')
        else:
            return render(request, 'registration.html', {'form': form})
    else:
            form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})










