from django.shortcuts import render, redirect
from django.views import View
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    
    return render(request,template_name="users/home.html")

class login_view(View):
    def get(self, request):
        form = forms.LoginForm()
        context = {
            "form": form,
        }
        return render(request, "users/login.html", context)
    
    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "users/home.html")
        context = {
            "forms":form,
        }
        return render(request, "users/home.html", context=context)

def sign_up(request):
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "users/home.html")
        return redirect("users:sign_up")
    else:
        form = forms.SignupForm()
        context = {
            "form":form,
        }
        return render(request, "users/signup.html", context=context)
    

@login_required(login_url='log_in')
def log_out(request):
    logout(request)
    return redirect("users:main")