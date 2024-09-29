from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sports/", views.sports, name="sports"),
    path("science/", views.science, name="science"),
    path("jp/", views.jp, name="jp"),
    path("fr/", views.fr, name="fr"),
]
