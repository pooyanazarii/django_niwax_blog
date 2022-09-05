from django.contrib.auth import authenticate ,login,logout
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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
        form = AuthenticationForm() 
        contex = {"form":form}
        return render(request, 'accounts/login.html',contex)
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_up(request):
    return render(request, 'accounts/signup.html')

