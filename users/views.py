from django.shortcuts import render, redirect
from .forms import UsersForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    return render(request, 'users/login.html')

def registerPage(request):
    form = UsersForm()

    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'New account was created!')

            return redirect('login')

    context= {'form': form}
    return render(request, 'users/register.html', context)

def logoutForm(request):
    logout(request)
    return redirect('login')