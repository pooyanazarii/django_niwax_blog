from django import template
from iblog.models import Post
register = template.Library()

@register.inclusion_tag("blog_pages/recent-post.html",name="recposts")
def recent_blog_post(arg=6):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    context_recent = {"posts":posts}
    return (context_recent)

