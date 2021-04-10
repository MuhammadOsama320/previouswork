from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login as user_login


# Create your views here.
from django.urls import reverse


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            user_login(request, user)
            return redirect(reverse("login"))
        return render(request, 'login.html',{})


def logout(request):
    logout(request)
    return redirect(reverse("login"))
