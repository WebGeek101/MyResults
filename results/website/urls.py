from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('', views.login),
    path('signup', views.signup),
    path('login', views.login),
    path('home', views.home),
    path('insertmarks', views.insertmarks),
    path('viewmarks', views.viewmarks),
    path('viewmarks/display',views.display,name="display"),
]
