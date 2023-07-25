from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse('«Домашка по 4 занятию»')

def main(response):
    return HttpResponse('Главная страница.')
