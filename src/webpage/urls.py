from django.urls import path
from .views import Home
from .views import Contact

urlpatterns = [
    path('', Home.as_view(), name='home'),
	#path(r'^contacto/$', Contact.as_view(), name='contact')
]
