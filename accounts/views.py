from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        users = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if users is not None:
            auth.login(request, users)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Email or Password is incorrect'})
    else:
        return render(request, 'accounts/login.html')



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
