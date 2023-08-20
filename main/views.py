from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    author = request.user
    print(author.username, author.email)
    return render(request, "main/index.html")


def get_started(request):
    return render(request, "main/get_started.html")


@login_required()
def user_profile(request):
    author = request.user
    events_organised = author.organiser.all()
    events_attended = author.attendees.all()

    return render(request, "main/profile.html", {
        "user": author,
        "organised_events": events_organised,
        "attended_events": events_attended
    })