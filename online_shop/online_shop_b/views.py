from django.shortcuts import render
from django.http import HttpResponse

def index(requests):
    return render(requests, 'index.html')

def top_sellers(requests):
    return render(requests, 'top-sellers.html')

def profile(requests):
    return render(requests, 'profile-net.html')

def adv_post(requests):
    return render(requests, 'advertisement-post.html')

def login(requests):
    return render(requests, 'login.html')

def register(requests):
    return render(requests, 'register.html')