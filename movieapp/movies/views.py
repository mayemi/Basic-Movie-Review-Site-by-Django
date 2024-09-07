from django.shortcuts import render
from .models import Category, Movie

kategoriListe = ["Macera", "Romantik", "Dram", "Bilim-Kurgu"]
filmListe = [
    {
        "id": 1,
        "film_adi": "Interstellar",
        "aciklama": "Dünya'nın en iyi filmi.",
        "image": "interstellar.jpg",
        "anasayfa": True
    },
    {
        "id": 2,
        "film_adi": "Fight Club",
        "aciklama": "Dünya'nın en iyi 2. filmi.",
        "image": "fc.jpg",
        "anasayfa": True
    },
    {
        "id": 3,
        "film_adi": "V for Vendetta",
        "aciklama": "Dünya'nın en iyi 3. filmi.",
        "image": "v4v.webp",
        "anasayfa": True
    },
    {
        "id": 4,
        "film_adi": "The Lord Of The Rings",
        "aciklama": "Dünya'nın en iyi 4. filmi.",
        "image": "lotr.jpg",
        "anasayfa": False
    },
    {
        "id": 5,
        "film_adi": "The Dark Knight",
        "aciklama": "Dünya'nın en iyi 5. filmi.",
        "image": "dn.jpg",
        "anasayfa": False
    },
]  # Listeler kullanılmadı çünkü admin paneliyle halledildi. Model oluşturuldu, admin paneliyle tablo dolduruldu ve veriler tabandan çekildi.

def home(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.filter(anasayfa=True),
    }
    return render(request, "index.html", data)

def movies(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movie.objects.all(),
    }   
    return render(request, "movies.html", data)

def moviedetails(request, id):
    data = {
        "movie": Movie.objects.get(id=id)
    }
    return render(request, "details.html", data)