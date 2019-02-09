from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('reg_success/', views.reg_success, name='reg_sucess'),
    path('unsub_success/', views.unsub_success, name='unsub_success'),
]
