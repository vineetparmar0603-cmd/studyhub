from django.urls import path
from . import views

urlpatterns = [
    path('', views.public_notes, name='public_notes'),
    path('upload/', views.upload_public_note, name='upload_public_note'),
]