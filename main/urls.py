from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="global_index")
]