
from django.shortcuts import render
from musician.models import Musician
from django.views.generic import ListView

class HomeView(ListView):
    template_name = 'home.html'
    model = Musician
    context_object_name = 'musicians'

    def get_queryset(self):
        return Musician.objects.prefetch_related('albums')

