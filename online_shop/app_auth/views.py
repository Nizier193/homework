from django.core.exceptions import ValidationError
from django.shortcuts import render

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .forms import UserForm

def login_(requests):
    profile_url = reverse('profile')
    if requests.method == 'GET':
        if requests.user.is_authenticated:
            return redirect(profile_url)
        else:
            return render(requests, 'app_auth/login.html', context={'authenticated':True if requests.user.is_authenticated else False})

    username = requests.POST['username']
    password = requests.POST['password']
    user = authenticate(requests, username=username, password=password)

    if user is not None:
        login(requests, user)
        return redirect(profile_url)

    context = {'error':'No user found.'}

    return render(requests, 'app_auth/login.html', context=context)

@login_required(login_url=reverse_lazy('login'))
def profile_(requests):
    context = {'user':requests.user, 'authenticated':True if requests.user.is_authenticated else False}
    return render(requests, 'app_auth/profile.html', context)

def register_(requests):
    if requests.method == 'POST':
        form = UserForm(requests.POST, requests.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.error_messages)
            return render(requests, 'app_auth/register.html', context={'authenticated':True if requests.user.is_authenticated else False, 'form':form, 'errors':form.errors})

        return redirect(reverse('register'))
    else:
        form = UserForm()
        return render(requests, 'app_auth/register.html', context={'authenticated':True if requests.user.is_authenticated else False, 'form':form, 'errors':form.errors})

def logout_view(requests):
    logout(requests)
    return redirect(reverse('login'))