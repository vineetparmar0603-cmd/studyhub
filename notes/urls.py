from django.urls import path
from . import views

urlpatterns = [
    path('', views.public_notes, name='public_notes'),
    path('upload/', views.upload_public_note, name='upload_public_note'),
    path('download/<int:note_id>/', views.download_note, name='download_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
]