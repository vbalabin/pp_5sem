from django.urls import path
from .views import photoPageView



urlpatterns = [
    path('', photoPageView, name='photo'),
]