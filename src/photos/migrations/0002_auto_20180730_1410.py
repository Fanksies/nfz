# Generated by Django 2.0.7 on 2018-07-30 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='camera',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='photo',
            name='collection',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Colección'),
        ),
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='descripción'),
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='photos/photos/', verbose_name='archivo'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(max_length=64, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='slug',
            field=models.CharField(max_length=64, verbose_name='slug'),
        ),
    ]
