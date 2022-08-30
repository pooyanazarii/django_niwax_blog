
from turtle import title
from django.db import models
from django.utils.html import format_html
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Tags(models.Model):
    nametag = models.CharField(max_length=255)
    def __str__(self):
        return self.nametag
class Post(models.Model):
    tags = models.ManyToManyField(Tags)
    image = models.ImageField(upload_to ='blog/',default = 'blog/default.jpg')
    title = models.CharField(max_length=255)
    text_content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null= True)
    category = models.CharField(max_length=255)
    counted_view = models.IntegerField()
    status = models.BooleanField()
    published_date = models.DateTimeField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        ordering=['id']
                
    def __str__(self):
        return self.title
