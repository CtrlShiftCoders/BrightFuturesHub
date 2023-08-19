from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="cf-home"),
    path('<slug:slug>/', views.details, name='cf-details'),
]
