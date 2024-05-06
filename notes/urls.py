from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesListView.as_view(), name='notes-list'),
    path('new', views.NotesCreateView.as_view(), name='notes-create'),
    path('<int:pk>', views.NotesDetailView.as_view(), name='notes-detail'),
]
