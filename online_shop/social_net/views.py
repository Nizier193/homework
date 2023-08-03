from django.shortcuts import render
from .models import *

def main_page(requests):
    announcements = Announcement.objects.all().order_by("-id")[:2][::-1]
    profile = Person.objects.all().get(id=1)
    return render(requests, 'main-net.html', {'profile':profile, 'announcements':announcements})

def profile_page(requests):
    profile = Person.objects.all().get(id=1)
    announcements = Announcement.objects.all().filter(person=profile.username).order_by("-id")[:2][::-1]

    friends = [Person.objects.all().get(username=friend) for friend in profile.friends]
    picture_main = profile.image[0]
    try:
        pictures = profile.image[1:]
        return render(requests, 'profile-net.html', {'profile':profile,
                                                     'announcements':announcements,
                                                     'profile_pic':picture_main,
                                                     'pictures':pictures,
                                                     'friends':friends
                                                     })
    except Exception:
        return render(requests, 'profile-net.html', {'profile':profile,
                                                     'announcements':announcements,
                                                     'profile_pic':picture_main,
                                                     'pictures':[],
                                                     'friends':friends
                                                     })

def register_page(requests):
    return render(requests, 'register-net.html')

def login_page(requests):
    return render(requests, 'login-net.html')