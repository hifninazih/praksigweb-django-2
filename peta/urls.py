from django.urls import path
from . import views

urlpatterns = [
    path("", views.LihatSuperHero, name="lihat_superhero"),
    path("create/", views.createSuperHero, name="tambah_superhero"),
    path("create/simpan/", views.simpanSuperHero, name="simpan"),
    path("delete/<int:id>/", views.deleteSuperHero, name="delete"),
    path("update/<int:id>/", views.updateSuperHero, name="update"),
    path(
        "update/simpan/<int:id>/",
        views.simpanUpdateSuperHero,
        name="simpan_update_superhero",
    ),
]
