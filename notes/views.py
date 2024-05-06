from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Notes
from .forms import NotesForm

# Create your views here.


class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/notes'
    template_name = 'notes/notes_form.html'


class NotesListView(ListView):
    model = Notes
    template_name = 'notes/notes_list.html'
    context_object_name = 'note'


class NotesDetailView(DetailView):
    model = Notes
    template_name = 'notes/notes_detail.html'
    context_object_name = 'note'
