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
    path('category=<str:getname>',blog_home_view,name="category"),
    path('author=<str:author_username>',blog_home_view,name="author"),
    path('search/',search_view,name='search'),
    # path('test2/',test2_view,name="test2"),
]
