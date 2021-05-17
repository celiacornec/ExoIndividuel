from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.accueil, name='accueil'),
    path('infoalbum/<int:album_id>', views.infoalbum, name='infoalbum'),
    #path('accueil/', views.filterform, name='filterform')
]