from django.contrib import admin
from django.urls import path
from . import views

#added include module for url mapping

urlpatterns = [
        path('', views.home, name = "home"),
]