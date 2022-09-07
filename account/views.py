from django.contrib.auth import authenticate ,login,logout 
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def login_view(request):
    # if request.user.is_authenticated:
    #     msg = f"is authenticated {request.user.username}"
    # else: 
    #     msg = f"is not authenticated"
    if not request.user.is_authenticated:
        if request.POST:
            form = AuthenticationForm(request=request , data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request,username = username , password = password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
                else:
                     messages.add_message(request, messages.SUCCESS, ' نام کاربری یا رمز عبود اشتباه وارد شده ')
        form = AuthenticationForm() 
        contex = {"form":form}
        return render(request, 'accounts/login.html',contex)
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
                messages.add_message(request, messages.SUCCESS, ' حساب کاربری شما با موفقیت ساخته شد. ')
                # return redirect(reverse("login"))
                return redirect(reverse("accounts:login"))

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