from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="main-page"),
    path('top-sellers/', top_sellers, name="top-sellers"),
    path('adv-post/', adv_post, name='advertisement-post'),
]