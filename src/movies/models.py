from django.db import models

# Create your models here.

class MovieRole(models.Model):
    name = models.CharField('nombre rol', max_length=32,)

class Movie(models.Model):

    class Meta:
        ordering = ['-year']

    name = models.CharField('movie', max_length=128,)
    slug = models.CharField('movie slug', max_length=128,)
    synopsis = models.TextField('sinopsis', null=True, blank=True,)
    year = models.CharField('año',max_length=64, null=True, blank=True,)
    country = models.CharField('pais', max_length=128, null=True, blank=True,)
    director = models.CharField('director', max_length=128, null=True, blank=True,)
    poster = models.FileField('poster', null=True, blank=True,)
    role = models.ManyToManyField('MovieRole')
    imdb_link = models.URLField('link IMDB', max_length=128, null=True, blank=True,)
    trailer_link = models.URLField('link trailer', max_length=128, null=True, blank=True,)

class MovieStill(models.Model):

    class Meta:
        ordering = ['order']

    name = models.CharField('nombre', max_length=128,)
    image = models.FileField('imagen', upload_to='movies/stills/', null=True, blank=True,)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    order = models.IntegerField('orden')

class MovieQuote(models.Model):

    movie = models.OneToOneField('Movie', on_delete=models.CASCADE)
    text = models.CharField('Texto Quote', null=True, blank=True, max_length=128,)
    author = models.CharField('Autor Quote', null=True, blank=True, max_length=64,)

