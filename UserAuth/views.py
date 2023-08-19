from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect


def login_user(request):
    if request.method == "POST":
        user_name = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=user_name, password=password)
        # users = User.objects.all()
        # print(user_name, password)
        # for user in users:
        #     print(f"email:{user.email} pass:{user.password} name: {user.username}")
        if user is not None:
            # login(request, user)
            return HttpResponseRedirect("/")
        else:
            print("hello")

    elif request.method == "GET":
        return render(request, "UserAuth/login.html")

def register_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        conf_password = request.POST["conf_password"]
        user_name = request.POST["username"]
        if conf_password == password:
            user = User.objects.create_user(username=user_name, password=password, email=email)
            return HttpResponseRedirect('/')
            # login(request, user)
        else:
            return HttpResponseRedirect(reverse("signup"))
    elif request.method == "GET":
        return render(request, "UserAuth/register.html")