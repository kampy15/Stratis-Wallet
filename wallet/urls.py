from django.contrib import admin
from django.urls import path
from wallet import views

urlpatterns = [
    path("",views.index, name='wallet')
]