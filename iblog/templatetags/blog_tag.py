from django import template

register = template.Library()

@register.simple_tag
def funplus (a):
    return a+2