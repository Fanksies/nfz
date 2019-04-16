from django.views.generic import DetailView, ListView
from .models import Photo

# Create your views here.

class PhotoDetail(DetailView):
    model = Photo

class PhotoList(ListView):
    model = Photo