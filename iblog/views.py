from django.shortcuts import render ,get_object_or_404
from iblog.models import Post
from datetime import datetime
from django.utils import timezone  

# Create your views here.
def blog_home_view(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now() ,status=1)
    context_home = {'posts':posts}
    return render(request,'blog_pages/blog-home.html',context_home)



def about_view(request):
    return render(request,'blog_pages/about.html')



def blog_single_view(request,pid):
    posts = get_object_or_404(Post,pk=pid,status=1)
    temp_viewed = posts.counted_view
    posts.counted_view = temp_viewed + 1
    posts.save()

    #------------------------------------ for next and previous 
    # this_post = Post.objects.get(id=pid)
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



def url_view_test(request,pid,nameurls):
    ur_context = {"pid":pid , 'nameurls':nameurls}
    return render(request , "test.html",ur_context)