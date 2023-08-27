from django.shortcuts import render, reverse, redirect

from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvForm

def index(requests):
    advertisements = Advertisement.objects.all().order_by('-id')
    return render(requests, 'app_advertisement/index.html', context={'advertisements':advertisements,
                                                                     'authenticated':True if requests.user.is_authenticated else False})

def top_sellers(requests):
    return render(requests, 'app_advertisement/top-sellers.html', context={'authenticated':True if requests.user.is_authenticated else False})

def adv_post(requests):
    print(requests)
    if requests.method == "POST":
        form = AdvForm(requests.POST, requests.FILES)
        if form.is_valid():
            if form.is_valid_title():
                advertisement = form.save(commit=False)
                advertisement.user = requests.user
                advertisement.save()

                url = reverse('main-page')
                return redirect(url)

    else:
        form = AdvForm()

    form = AdvForm()
    return render(requests, 'app_advertisement/advertisement-post.html', context={'form':form, 'authenticated':True if requests.user.is_authenticated else False})