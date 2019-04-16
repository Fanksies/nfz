from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from movies.models import Movie
from photos.models import Photo

# Create your views here.

class Home(TemplateView):
	template_name = 'webpage/index.html'

	def get_context_data(self, **kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['featured_movies']= Movie.objects.all()[:8]
		context['featured_photos']=Photo.objects.filter(is_featured=True)[:12]
		return context

class Contact(TemplateView):
    template_name = 'webpage/contact.html'
