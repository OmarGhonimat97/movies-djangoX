from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Movie
# Create your views here.


class MovieListView(ListView):
    template_name = 'movies/movie_list.html'
    model = Movie


class MovieDetailView(DetailView):
    template_name = 'movies/movie_detail.html'
    model = Movie


class MovieCreateView(CreateView):
    template_name = 'movies/movie_create.html'
    model = Movie
    fields = ['name', 'user', 'description']


class MovieUpdateView(UpdateView):
    template_name = 'movies/movie_update.html'
    model = Movie
    fields = ['name', 'user', 'description']


class MovieDeleteView(DeleteView):
    template_name = 'movies/movie_delete.html'
    model = Movie
    success_url = reverse_lazy('movie_list')


