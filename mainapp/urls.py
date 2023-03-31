from django.contrib import admin
from django.urls import path, include
from mainapp.views import MainListView, ColorListView, ServiceListView, EmailView

app_name = 'mainapp'

urlpatterns = [
    path('', MainListView.as_view(), name='index'),
    path('color/', ColorListView.as_view(), name='color'),
    # path('service/', ServiceListView.as_view(), name='service'),
    path('email/', EmailView.as_view(), name='send_email'),
]
