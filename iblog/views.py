from django.shortcuts import render
from iblog.models import Post

# Create your views here.
def blog_home_view(request):
    posts = Post.objects.all()
    context_home = {'posts':posts}
    return render(request,'blog_pages/blog-home.html',context_home)

def about_view(request):
    return render(request,'blog_pages/about.html')

def blog_single_view(request):
    return render(request, 'blog_pages/blog-single.html')

def error_view(request):
    return render(request, 'blog_pages/error.html')

def blog_home_static_view (request):
    return render(request,"blog_pages/blog-home-static.html")

def url_view_test(request,nameurl):

    return render(request , "test.html",{'urladd':nameurl})