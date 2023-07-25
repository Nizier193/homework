from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('lesson_4', main)
]