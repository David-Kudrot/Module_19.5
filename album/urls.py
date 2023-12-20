from django.urls import path
from .views import AlbumCreateView, AlbumDeleteView, UpdateAlbum


urlpatterns = [
    path('create_album/', AlbumCreateView.as_view() , name='album'),
    path('edit/<int:id>', UpdateAlbum.as_view(), name='edit_album'),
    path('delete/<int:id>', AlbumDeleteView.as_view(), name='delete_album'),
]
