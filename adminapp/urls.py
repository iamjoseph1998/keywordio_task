from django import views
from django.urls import path
from . import views

app_name = 'adminapp'

urlpatterns = [
    path('home', views.home, name='home'),
    path('addbook', views.addbook, name='addbook'),
    path('updatebook', views.updatebook, name='updatebook'),
    path('deletebook', views.deletebook, name='deletebook'),
]
