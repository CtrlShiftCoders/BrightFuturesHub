from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required()
def index(request):
    if request.method == "POST":
        new_event = Event(
                title=request.POST.get("title"),
                event_description=request.POST.get("description"),
                event_start_time=request.POST.get("time"),
                event_duration=request.POST.get("duration"),
                event_date=request.POST.get("date"),
                type=request.POST.get("type")
                )
        new_event.save()

        return HttpResponseRedirect(reverse("comm-home"))
    upcoming_events = Event.objects.filter(status="Upcoming").order_by("-event_date")
    return render(request, "Community/index.html", {"upcoming_events": upcoming_events})


@login_required()
def details(request, slug):
    event = get_object_or_404(Event, slug=slug)
    if request.method == "POST":
        attendee = int(request.POST.get("attendee"))
        event.attendees += attendee
        event.save()
        return HttpResponseRedirect(reverse("comm-details"), slug=slug)

    return render(request, 'Community/details.html', {'event': event})


