from django.contrib import admin
from django.urls import path
from website.views import *

app_name = "website"
urlpatterns = [
    path('contact',contactus_view,name='contact'),
]