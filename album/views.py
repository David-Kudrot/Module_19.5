from django.shortcuts import render,  redirect
from album.forms import AlbumForm
from album.models import Album
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('album')
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class UpdateAlbum(UpdateView):
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('home')
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    
    def form_valid(self, form):
        return super().form_valid(form)
    
class AlbumDeleteView(DeleteView):
    model = Album
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        album = self.get_object()
        album.delete()
        return redirect(self.success_url)