from django.contrib.auth import authenticate ,login
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def login_view(request):
    # if request.user.is_authenticated:
    #     msg = f"is authenticated {request.user.username}"
    # else: 
    #     msg = f"is not authenticated"
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username = username , password = password)
        if user is not None:
            login(request,user)
            return redirect('/')

        print("------------------------------")
    return render(request, 'accounts/login.html')

# def logout_view(request):
#     pass

def signup_up(request):
    return render(request, 'accounts/signup.html')

