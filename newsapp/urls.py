from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("sports/", views.sports),
    path("science/", views.science),
]
