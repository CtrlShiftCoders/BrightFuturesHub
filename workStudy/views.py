from django.shortcuts import render
from .models import Jobs

def index(request):
    jobs=Jobs.objects.all()
    return render(request,"workStudy/index.html",{
        "jobs":jobs
        })

def job_details(request,slug):
    job=Jobs.objects.get(job_slug=slug)
    return render(request,"workStudy/job_details.html",{'job':job})
    
