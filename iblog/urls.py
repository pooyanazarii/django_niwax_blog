from django.contrib import admin
from django.urls import path
from iblog.views import *

urlpatterns = [
    path('blog-home',blog_home_view)
]
