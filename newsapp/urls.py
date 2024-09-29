from django.urls import path
from . import views

urlpatterns = [
    path("sports/", views.sports),
    path("science/", views.science),
]
