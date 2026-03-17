from django.urls import path
from . import views

urlpatterns = [
    path('', views.group_list, name='group_list'),
    path('create/', views.create_group, name='create_group'),
    path('join/<int:group_id>/', views.join_group, name='join_group'),
    path('<int:group_id>/', views.group_detail, name='group_detail'),
    path('upload_note/<int:group_id>/', views.upload_note, name='upload_note'),
    path('chat/<int:group_id>/', views.group_chat, name='group_chat'),
    path('groups/<int:group_id>/members/', views.group_members, name='group_members'),
]