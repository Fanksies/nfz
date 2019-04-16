from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Movie
# Create your views here.

class MovieDetail(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'

class MovieList(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'


