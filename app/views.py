from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    template_name = 'index.html'


class ListeFilmsView(TemplateView):
    template_name = 'liste_films.html'

