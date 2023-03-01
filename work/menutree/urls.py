from django.contrib import admin
from django.urls import path
from . import views

app_name = 'menutree'
urlpatterns = [
    path('', views.show_menu, name='menu'),
    path('', views.index, name='menu'),
]