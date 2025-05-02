from django.shortcuts import render
from .models import Superhero
import json


def LihatSuperHero(request):
    # Ambil data superhero dengan asosiasi 'Y'
    # SemuaHero = Superhero.objects.filter(asosiasi="Y").values('nama', 'asosiasi', 'lat', 'long')
    SemuaHero = Superhero.objects.all().values(
        "nama", "asosiasi", "lat", "long", "deskripsi"
    )
    # Ubah queryset menjadi list of dictionaries dan konversi Decimal ke float
    SemuaHeroList = list(SemuaHero)
    for hero in SemuaHeroList:
        hero["lat"] = float(hero["lat"])
        hero["long"] = float(hero["long"])

    # Kirim data ke template dalam format JSON
    context = {"SemuaHero": json.dumps(SemuaHeroList)}

    return render(request, "peta/index.html", context)
