from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.accueil),
    path('infoalbum', views.infoalbum, name = 'informations album')
]