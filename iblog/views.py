from django.shortcuts import render ,get_object_or_404
from iblog.models import Post

# Create your views here.
def blog_home_view(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(published_date__lte="2022-9-03 12:00:00")
    context_home = {'posts':posts}
    return render(request,'blog_pages/blog-home.html',context_home)

def about_view(request):
    return render(request,'blog_pages/about.html')

def blog_single_view(request,pid):
    posts = get_object_or_404(Post,pk=pid)
    context_singel_post = {'posts':posts}
    return render(request, 'blog_pages/blog-single.html',context_singel_post)

def error_view(request):
    return render(request, 'blog_pages/error.html')

def blog_home_static_view (request):
    return render(request,"blog_pages/blog-home-static.html")

def url_view_test(request,pid,nameurls):
    ur_context = {"pid":pid , 'nameurls':nameurls}
    return render(request , "test.html",ur_context)