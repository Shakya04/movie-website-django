from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
# Create your views here.


def register(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save()

            #firstpassword
            first_password = form.cleaned_data.get('password1')

            #authenticate
            user = authenticate(username=user, password=first_password)

            #login
            login(request, user)

            return redirect("movie_site:home")
    else:
        form = Registration()
    return render(request, "register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("movie_site:home")
            else:
                return render(request, 'login.html', {"error": "Your acc is disabled"})
        else:
            return render(request, "login.html", {"error": "Invalid Username or password."})
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect("movie_site:home")