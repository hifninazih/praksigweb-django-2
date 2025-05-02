from django.urls import path
from . import views

urlpatterns = [
    path("", views.LihatSuperHero, name="lihat_superhero"),
]
