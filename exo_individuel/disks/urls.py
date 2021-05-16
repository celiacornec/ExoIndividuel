from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.accueil, name='accueil'),
    path('infoalbum/<int:album>', views.infoalbum, name='infoalbum'),
]