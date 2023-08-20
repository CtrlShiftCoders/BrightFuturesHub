from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="ws-index"),        
    path('<slug:slug>',views.job_details,name="ws-details")        
]
