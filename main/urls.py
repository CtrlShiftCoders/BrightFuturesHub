from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_started, name="get_started"),
    path("index/", views.index, name="global_index"),
    path("my_profile/", views.user_profile, name="user_profile"),
    path("about_us/",views.about, name="about"),
]
