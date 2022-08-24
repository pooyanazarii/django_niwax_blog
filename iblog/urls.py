from django.contrib import admin
from django.urls import path
from iblog.views import *

urlpatterns = [
    path('',blog_home_view,name='blog-home'),
    path('about',about_view,name='about'),
    path('blog_single',blog_single_view,name='blog_single'),
    path('error',error_view,name='error'),
]
