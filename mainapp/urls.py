from django.contrib import admin
from django.urls import path, include
from mainapp.views import MainListView, ColorListView

app_name = 'mainapp'

urlpatterns = [
    path('', MainListView.as_view(), name='index'),
    path('colors/', ColorListView.as_view(), name='color'),
]