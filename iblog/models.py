from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    text_content = models.TextField()
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    #tag
    counted_view = models.IntegerField()
    status = models.BooleanField()
    published_date = models.DateTimeField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()


