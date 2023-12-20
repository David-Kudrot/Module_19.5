from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from musician.forms import MusicianForm
from musician.models import Musician
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.


class MusicianView(CreateView):
    model = Musician
    form_class = MusicianForm
    success_url = reverse_lazy('musician')
    template_name = 'musician.html'
    
    def form_valid(self, form):
        return super().form_valid(form)


class EditMusicianView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        return super().form_valid(form)
    
 