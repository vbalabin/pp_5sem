from django import urls
from django.urls import path
from .views import index, addemployee

urlpatterns = [
    path('', index, name='main'),
    path('main/', index),
    path('add/', addemployee, name='add')
]