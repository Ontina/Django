from django.urls import path
from .views import fetchfood,createfood

urlpatterns = [
  path("allfood/", fetchfood),
  path("createfood/", createfood)
]