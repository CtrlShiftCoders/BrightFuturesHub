from django.urls import path
from . import views

<<<<<<< HEAD
urlpatterns=[
    path("", views.index, name="comm-home")
]
=======
urlpatterns = [
    path("", views.index, name="comm-home"),
    path('<slug:slug>/', views.details, name="comm-details"),

]
>>>>>>> source/main
