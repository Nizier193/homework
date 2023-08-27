from django import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_, name='register'),
    path('login/', login_, name='login'),
    path('profile/', profile_, name='profile'),
    path('logout/', logout_view, name='logout')
]