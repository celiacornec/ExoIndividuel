from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.accueil),
    path('infoalbum/<int:album>', views.infoalbum, name='infoalbum'),
]
