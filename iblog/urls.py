from django.contrib import admin
from django.urls import path
from iblog.views import *
app_name = "blog"
urlpatterns = [
    path('',blog_home_view,name='blog-home'),
    path('about',about_view,name='about'),
    path('postid=<int:pid>',blog_single_view,name='blog_single'),
    path('error',error_view,name='error'),
    path('blog_home_static',blog_home_static_view,name='blog_home_static'),
    path('test',url_view_test,name="test"),
    path('category=<str:getname>',blog_cat_view,name="category"),
]
