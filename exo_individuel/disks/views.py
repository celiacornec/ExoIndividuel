from django.shortcuts import render
from .models import Album

# Create your views here.

def accueil(request):
    albums = Album.objects.all()
    return render(request, 'disks/accueil.html', locals())

def infoalbum(request):
    return render(request, 'disks/infoalbum.html')