from django.shortcuts import render, reverse, redirect

from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvForm

def index(requests):
    advertisements = Advertisement.objects.all().order_by('-id')
    return render(requests, 'index.html', context={'advertisements':advertisements})

def top_sellers(requests):
    return render(requests, 'top-sellers.html')

def profile(requests):
    return render(requests, 'profile-net.html')

def adv_post(requests):
    print(requests)
    if requests.method == "POST":
        form = AdvForm(requests.POST, requests.FILES)
        if form.is_valid():
            if form.is_valid_title():
                advertisement = Advertisement(**form.cleaned_data)
                advertisement.user = requests.user
                advertisement.save()

                url = reverse('main-page')
                return redirect(url)

    else:
        form = AdvForm()

    form = AdvForm()
    return render(requests, 'advertisement-post.html', context={'form':form})

def login(requests):
    return render(requests, 'login.html')

def register(requests):
    return render(requests, 'register.html')