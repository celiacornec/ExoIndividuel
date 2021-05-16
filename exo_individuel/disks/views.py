from django.shortcuts import render
from .models import Album, Track, Artist
from .forms import FilterForm

# Create your views here.

def accueil(request):
    albums = Album.objects.all()
    return render(request, 'disks/accueil.html', locals())

def infoalbum(request, album):
    #album = Album.objects.filter(id=album)
    tracks = Track.objects.filter(album=album)
    artist = Artist.objects.get(album=album)
    return render(request, 'disks/infoalbum.html', locals())

def filterform(request):
    form = FilterForm(request.POST or None)
    if form.is_valid():
        recherche = form.cleaned_data['recherche']
        albums_filtered = Album.objects.filter(title__contains=recherche)
    return render(request, 'disks/filterform.html', locals())


