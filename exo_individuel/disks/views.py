from django.shortcuts import render
from .models import Album, Track, Artist
from .forms import FilterForm

# Create your views here.

def accueil(request):
    albums = Album.objects.all()
    form = FilterForm(request.POST or None)
    if form.is_valid():
        recherche = form.cleaned_data['recherche']
        albums = Album.objects.filter(title__contains=recherche)
    return render(request, 'disks/accueil.html', locals())

def infoalbum(request, album_id):
    album = Album.objects.get(id=album_id)
    tracks = Track.objects.filter(album__id=album_id)
    artist = Artist.objects.get(album__id=album_id)
    return render(request, 'disks/infoalbum.html', locals())




