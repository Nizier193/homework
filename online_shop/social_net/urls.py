from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main-page-net'),
    path('profile/', profile_page, name='profile-page-net'),
    path('register/', register_page, name='register-page-net'),
    path('login/', login_page, name='login-page-net')
]