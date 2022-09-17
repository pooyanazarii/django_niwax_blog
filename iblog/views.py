
from django.shortcuts import render, get_object_or_404
from iblog.models import Post, Comment
# from iblog.models import Post
from datetime import datetime
from django.utils import timezone
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage
from datetime import datetime
# from iblog.forms import NameFrom
# from iblog.forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
from iblog.forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.


def blog_home_view(request, **kwargs):
    print(kwargs)
    print("-----------------------------------------------")
    # posts = Post.objects.all()
    posts = Post.objects.filter(published_date__lte= timezone.now(), status=1)
    if kwargs.get("getname"):
        posts = posts.filter(tags__nametag=kwargs["getname"])
    if kwargs.get("author_username"):
        posts = posts.filter(author__username=kwargs["author_username"])
    
    # pagenumber = 1
    # if pagenumber := request.GET.get('page'):
        # pass
    # Paginator
    posts = Paginator(posts,6)
    try:
        
        posts = posts.get_page(request.GET.get('page'))
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

        
    context_home = {'posts': posts}
    return render(request, 'blog_pages/blog-home.html', context_home)


def about_view(request):
    return render(request, 'blog_pages/about.html')

# @login_required
def blog_single_view(request, pid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'دیدگاه شما با موفقیت ثبت شد')
        else:
            #message
            messages.add_message(request, messages.ERROR, 'عملیات با شکست مواجه شد.')

    else:
        pass
    posts = Post.objects.filter(status=1)
    posts = get_object_or_404(Post, pk=pid)

    temp_viewed = posts.counted_view
    posts.counted_view = temp_viewed + 1
    posts.save()
    # ------------------------------------ for next and previous
    previous_post = Post.objects.filter(id__lt=pid, status=1).order_by('id').last()
    next_post = Post.objects.filter(id__gt=pid, status=1).order_by('id').first()
    if previous_post == None: previous_post = {"id": 0}
    if next_post == None: next_post = {"id": 0}

    print("-show login req post----------------------------------------------", not posts.login_require)
    print("-authen----------------------------------------------",request.user.is_authenticated)
    if posts.login_require:
        if request.user.is_authenticated:
            form = CommentForm()
            comment = Comment.objects.filter(post=posts.id,approved=True).order_by('-created_date')
            context_singel_post = {'posts': posts,'next': next_post, 'prev': previous_post,'comments':comment , 'form':form}
            return render(request, 'blog_pages/blog-single.html', context_singel_post)
        else:
            print("ACCOUNT OUT-----------------------")
            return HttpResponseRedirect(reverse("accounts:login"))  
    else:
        form = CommentForm()
        comment = Comment.objects.filter(post=posts.id,approved=True).order_by('-created_date')
        context_singel_post = {'posts': posts,'next': next_post, 'prev': previous_post,'comments':comment , 'form':form}
        return render(request, 'blog_pages/blog-single.html', context_singel_post)
        
        


def error_view(request):
    return render(request, 'blog_pages/error.html')


def blog_home_static_view(request):
    return render(request, "blog_pages/blog-home-static.html")


def url_view_test(request):
    return render(request, "test.html")

# def blog_cat_view(request,getname):
#     # posts = Post.objects.all()
#     posts = Post.objects.filter(status=1)
#     posts  = posts.filter(tags__nametag=getname)
#     context_home = {'posts':posts}
#     return render(request,'blog_pages/blog-home.html',context_home)


def search_view(request):
    print("--------------------------------")
    print(request.__dict__)
    posts = Post.objects.filter(status=1)
    search_value = "جست و جو نتیجه ای  نداشت!"
    if search_value := request.GET.get("s"):
        posts = posts.filter(text_content__contains=search_value)

    context_search = {"posts": posts, "searchkey": search_value}
    return render(request, "blog_pages/blog-home.html", context_search)


# def test2_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         # name =(request.POST.get("name"))
#         # email =(request.POST.get("email"))
#         # subject =(request.POST.get("subject"))
#         # message =(request.POST.get("message"))
#         # print(name,email,subject,message)
#         # contact = Contact()
#         # contact.name = name
#         # contact.email = email
#         # contact.subject = subject
#         # contact.message = message
#         # contact.created_date =datetime.now()
#         # contact.updated_date = datetime.now()
#         # contact.save()
#         if form.is_valid():
#             # name = form.cleaned_data['name']
#             # subject = form.cleaned_data['subject']
#             # email = form.cleaned_data['email']
#             # message = form.cleaned_data['message']
#             # print(name,email,subject,message)
#             form.save()
#             messages.add_message(request,messages.SUCCESS,'Your ticekt ok')
#             return HttpResponse("done")
#         else:
#             messages.add_message(request,messages.ERROR,'noooooooooo')
#             return HttpResponse("no valied")
#     form = ContactForm()
#     return render(request,"test2.html",{'form':form})


def handler404(request, exception):
    context = {}
    response = render(request, "blog_pages/error.html", context=context)
    response.status_code = 404
    return response