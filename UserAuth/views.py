from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("global_index"))
            else:
                return HttpResponseRedirect(reverse("login"))
    else:
        form = LoginForm()

    return render(request, "registration/login.html", {'form': form})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("global_index"))
    else:
        form = SignupForm()

    return render(request, "registration/register.html", {'form': form})
@login_required()
def Logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
