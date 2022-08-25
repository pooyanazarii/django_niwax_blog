from django.shortcuts import render

# Create your views here.
def blog_home_view(request):
    return render(request,'blog_pages/blog-home.html')

def about_view(request):
    return render(request,'blog_pages/about.html')

def blog_single_view(request):
    return render(request, 'blog_pages/blog-single.html')

def error_view(request):
    return render(request, 'blog_pages/error.html')

def blog_home_static_view (request):
    return render(request,"blog_pages/blog-home-static.html")