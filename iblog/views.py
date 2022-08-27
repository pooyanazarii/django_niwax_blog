from django.shortcuts import render ,get_object_or_404
from iblog.models import Post
from datetime import datetime
from django.utils import timezone  

# Create your views here.
def blog_home_view(request,**kwargs):
    print (kwargs)
    print ("-----------------------------------------------")
    # posts = Post.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now() ,status=1)
    if kwargs.get("getname"):
        posts  = posts.filter(tags__nametag=kwargs["getname"])
    if kwargs.get("author_username"):
        posts  = posts.filter(author__username=kwargs["author_username"])
    context_home = {'posts':posts}
    return render(request,'blog_pages/blog-home.html',context_home)



def about_view(request):
    return render(request,'blog_pages/about.html')



def blog_single_view(request,pid):
    print("----------------------------------------")
    posts = Post.objects.filter(status=1)
  
    posts = get_object_or_404(Post,pk=pid)

    temp_viewed = posts.counted_view
    posts.counted_view = temp_viewed + 1
    posts.save()

    #------------------------------------ for next and previous 
    this_post = Post.objects.get(id=pid)
    previous_post = Post.objects.filter(id__lt=pid,status=1).order_by('id').last()
    next_post = Post.objects.filter(id__gt=pid,status=1).order_by('id').first()
    if previous_post== None :
        previous_post ={"id":0}
    if next_post== None :
        next_post ={"id":0}

    
    context_singel_post = {'posts':posts,'next':next_post,'prev':previous_post}    
        
    return render(request, 'blog_pages/blog-single.html',context_singel_post)



def error_view(request):
    return render(request, 'blog_pages/error.html')



def blog_home_static_view (request):
    return render(request,"blog_pages/blog-home-static.html")



def url_view_test(request):
    return render(request , "test.html")


# def blog_cat_view(request,getname):
#     # posts = Post.objects.all()
#     posts = Post.objects.filter(status=1)
#     posts  = posts.filter(tags__nametag=getname)
#     context_home = {'posts':posts}
#     return render(request,'blog_pages/blog-home.html',context_home)