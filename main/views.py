from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@login_required()
def index(request):
    author = request.user
    print(author.username, author.email)
    return render(request, "main/index.html")

@never_cache
def get_started(request):
    return render(request, "main/get_started.html")


@login_required()
def user_profile(request):
    author = request.user
    events_organised = author.organiser.all()
    events_attended = author.attendees.all()
    work_done= author.job_applications.all()

    return render(request, "main/profile.html", {
        "user": author,
        "organised_events": events_organised,
        "attended_events": events_attended,
        "work_done":work_done,
    })

def about(request):
    return render(request,"main/AboutUs.html")
