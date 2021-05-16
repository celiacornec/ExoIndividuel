from django.shortcuts import render
from .models import Album, Track, Artist

# Create your views here.

def accueil(request):
    albums = Album.objects.all()
    return render(request, 'disks/accueil.html', locals())

def infoalbum(request, album):
    tracks = Track.objects.filter(album=album)
   # unit_prices = []
   # for track in tracks:
 #       unit_prices = unit_prices + track.unit_price
    artist = Artist.objects.get(album=album)
    return render(request, 'disks/infoalbum.html', locals())