from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Fund


@login_required
@never_cache
def index(request):
    if request.method == "POST":
        new_fund = Fund(
            user=request.user,
            title=request.POST.get("title"),
            content=request.POST.get("description"),
            goal=request.POST.get("goal"),
            event_datetime=timezone.now()
        )
        new_fund.save()
        return redirect("cf-home")
    active_funds = Fund.objects.filter(status="In Progress").order_by("-event_datetime")
    return render(request, "crowdFunding/index.html", {"active_funds": active_funds})


@login_required
@never_cache
def details(request, slug):
    fund = get_object_or_404(Fund, slug=slug)
    if request.method == "POST":
        donation = int(request.POST.get("donation"))
        fund.amount_gained += donation
        if fund.amount_gained >= fund.goal:
            fund.status = "close"
        fund.save()
        return redirect("cf-details", slug=slug)

    return render(request, 'crowdFunding/details.html', {'fund': fund})
