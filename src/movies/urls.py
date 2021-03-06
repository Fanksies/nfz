from django.urls import path
from .views import MovieDetail, MovieList


urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<slug:slug>/', MovieDetail.as_view(), name='movie_detail'),
]
