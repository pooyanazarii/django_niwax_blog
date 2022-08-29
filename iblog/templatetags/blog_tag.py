from django import template
from iblog.models import Post,Tags
register = template.Library()

@register.simple_tag
def funplus (a):
    return a+2

@register.simple_tag(name='totlaposts')
def allpost ():
    return Post.objects.filter(status=1)

@register.filter
def snippet(value,arg=5):
    return value[:arg]+"..."

# @register.inclusion_tag('popularposts.html') # more used
# def popularposts_test():
#     posts = Post.objects.filter(status=1).order_by('-published_date')[:1]
#     return {'posts': posts}


@register.inclusion_tag('popularlatestpost.html')
def popularposts(arg=2):
    posts = Post.objects.filter(status=1).order_by('-counted_view')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog_pages/blog-latest-news.html',name="mylastpost")
def bloglatest(arg=2):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag("blog_pages/blog-category.html")
def category_post():
    posts  = Post.objects.filter(status=1)
    categories = Tags.objects.all()
    cat_dict={}
    for name in categories:
        count = posts.filter(tags=name).count()
        cat_dict[name]=count

    return {"categories":cat_dict}
