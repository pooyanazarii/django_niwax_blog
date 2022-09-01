
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255,null = True)
    email = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__ (self):
        return str(self.subject)+str(" -from-> ")+str(self.email)

