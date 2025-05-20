from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("flag/", views.flag, name="flag"),
    path("authenticate/", views.authenticate_user, name="authenticate_user"),
]