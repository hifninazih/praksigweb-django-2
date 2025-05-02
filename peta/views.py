from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Superhero
import json


def LihatSuperHero(request):
    SemuaHero = Superhero.objects.all().values(
        "nama", "asosiasi", "lat", "long", "deskripsi", "id"
    )
    # Ubah queryset menjadi list of dictionaries dan konversi Decimal ke float
    SemuaHeroList = list(SemuaHero)
    for hero in SemuaHeroList:
        hero["lat"] = float(hero["lat"])
        hero["long"] = float(hero["long"])

    # Kirim data ke template dalam format JSON
    context = {"SemuaHero": json.dumps(SemuaHeroList)}

    return render(request, "peta/index.html", context)


def createSuperHero(request):
    return render(request, "peta/create.html")


def simpanSuperHero(request):
    superhero = Superhero()
    superhero.nama = request.POST["nama"]
    superhero.lat = request.POST["lat"]
    superhero.long = request.POST["long"]
    superhero.asosiasi = request.POST["asosiasi"]
    superhero.deskripsi = request.POST["deskripsi"]
    superhero.save()
    messages.success(request, "Superhero berhasil disimpan")

    return redirect("tambah_superhero")


def deleteSuperHero(request, id):
    hero = Superhero.objects.get(id=id)
    hero.delete()
    messages.success(request, "Superhero berhasil dihapus")
    return redirect("/peta")


def updateSuperHero(request, id):
    hero = Superhero.objects.get(id=id)
    context = {"hero": hero}
    return render(request, "peta/update.html", context)


def simpanUpdateSuperHero(request, id):
    hero = Superhero.objects.get(id=id)
    hero.nama = request.POST["nama"]
    hero.lat = request.POST["lat"]
    hero.long = request.POST["long"]
    hero.asosiasi = request.POST["asosiasi"]
    hero.deskripsi = request.POST["deskripsi"]
    hero.save()
    messages.success(request, "Superhero berhasil diupdate")
    return redirect("/peta")
