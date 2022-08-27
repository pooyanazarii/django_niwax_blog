from django import template
from iblog.models import Post
register = template.Library()

@register.simple_tag
def funplus (a):
    return a+2

@register.simple_tag(name='totlaposts')
def allpost ():
    return Post.objects.filter(status=1)