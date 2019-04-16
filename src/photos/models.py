from django.db import models

# Create your models here.

class Photo(models.Model):

    name = models.CharField('nombre', max_length=64,)
    slug = models.CharField('slug',max_length=64,)
    image = models.FileField('archivo', upload_to='photos/photos/', null=True, blank=True,)
    collection = models.CharField('Colección',max_length=64, null=True, blank=True,)
    description = models.CharField('descripción',max_length=64, null=True, blank=True,)
    camera = models.CharField('slug',max_length=64, null=True, blank=True,)
    is_featured = models.BooleanField('Featured?', default=False)
