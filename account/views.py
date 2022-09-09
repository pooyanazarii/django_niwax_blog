from os import access
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from account.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def my_login(req,input,password):
    user = authenticate(req,username = input , password = password)
    print("=======","=======","=======","=======",user)
    if user is not None:
        login(req,user)
        return redirect(reverse("blog:blog-home"))
    else:
        messages.add_message(req, messages.SUCCESS, ' نام کاربری/ایمیل یا رمز عبود اشتباه وارد شده ')
        return redirect(reverse("accounts:login"))

        

def login_view(request):
    # email(request)
    if request.POST:
        form = AuthenticationForm(request=request , data = request.POST)
        
        print(form.is_valid())

        input_u = form.cleaned_data.get("username")
        
        if '@' in input_u:
            try:
                user = get_user_model().objects.get(email=input_u)
                username= user.username
                password = form.cleaned_data.get('password')
                return my_login(request,username,password)
            except:
                messages.add_message(request, messages.SUCCESS, ' نام کاربری/ایمیل یا رمز عبود اشتباه وارد شده ')
                        
        elif form.is_valid():
            print("=AAAAAAAAAAAAAAA")                
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')    
            return my_login(request,username,password)
        else:
            messages.add_message(request, messages.SUCCESS,  ' نام کاربری/ایمیل یا رمز عبود اشتباه وارد شده ')

            


    form = AuthenticationForm()
    contex = {"form": form}
    return render(request, 'accounts/login.html', contex)

def login_view1(request):
    if not request.user.is_authenticated:
        if request.POST:
            form = AuthenticationForm(request=request, data=request.POST)
            print("============================================before")
            if form.is_valid():
                print("============================================after")
                pass


        form = AuthenticationForm()
        contex = {"form": form}
        return render(request, 'accounts/login.html', contex)
    else:
        return redirect('/')



@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:

        forms = UserCreationForm
        if request.method == "POST":
            forms = UserCreationForm(request.POST)
            
            if forms.is_valid():
                
                forms.save()
                # messages.add_message(request, messages.SUCCESS, ' حساب کاربری شما با موفقیت ساخته شد. ')
                # return redirect(reverse("login"))
                return render(request,'accounts/signup_done.html')

        context = {"forms":forms}
        return render(request, 'accounts/signup.html',context)
    else:
        return redirect ("/")

# def passreset_view (request):
#     form_rest = form_rest = PasswordResetForm(None, request.POST)
#     if request.method == "POST":
#         print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
#         print(request.POST.get("csrfmiddlewaretoken"))
#         if form_rest.is_valid():
#             print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    
#     context = {'form':form_rest}
#     return render (request,'accounts/pass_reset_form.html',context)

# def email(request):
#     subject = 'ایمیل بازیابی'
#     message = ' رمز بازیابیش ما '
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['pya.nzri@gmail.com',]
#     send_mail( subject, message, email_from, recipient_list )
#     return redirect('/')

