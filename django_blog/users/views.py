from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login,authenticate, logout
from django.contrib import messages


# Create your views here.

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request, user)
            messages.success(request, "Register Successfully")
            return redirect("posts")
        
    else:
        form = RegisterForm()
    return render(request, "register.html",{'form':form})

def sign_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f"Hi {username.title()}, welcome back!")
                return redirect("posts")
            else:
                messages.error(request, "Invalid username or password")
                return redirect("login")
    else:
        form = LoginForm()
    return render(request,"login.html",{'form':form})
    
def sign_out(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

