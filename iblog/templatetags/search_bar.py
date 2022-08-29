from django import template
from iblog.models import Post
register = template.Library()

@register.inclusion_tag("blog_pages/search_bar.html",name="searchbar")
def searchbar():
    context_recent = {"posts":5}
    return (context_recent)
