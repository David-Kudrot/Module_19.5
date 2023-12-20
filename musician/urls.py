from django.urls import path
from .views import EditMusicianView, MusicianView

urlpatterns = [
    path('add/', MusicianView.as_view(), name='musician'),
    path('edit/<int:id>', EditMusicianView.as_view(), name='edit_musician'),
]
