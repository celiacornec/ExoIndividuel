from django import forms
from django.shortcuts import render

from .models import Album, Track, Artist

class FilterForm(forms.Form):
    recherche = forms.CharField(max_length=200)

