from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Jobs,JobApplication

def index(request):
    jobs=Jobs.objects.all()
    return render(request,"workStudy/index.html",{
        "jobs":jobs
        })

def job_details(request,slug):
    job=Jobs.objects.get(job_slug=slug)
    if request.method=="POST":
        
        # Checking if user has already not applied for the job
        if JobApplication.objects.filter(user=request.user).filter(job=job).exists():
            messages.error(request,"You have already registered for this event!")
        else:
            application= JobApplication(user=request.user,job=job)
            application.save()
            messages.success(request, f"You have registered for the {job.type} successfully,\
                    You will recieve an email from our partners soon.")
        return redirect("ws-details",slug=slug)    

    return render(request,"workStudy/job_details.html",{'job':job})
    
