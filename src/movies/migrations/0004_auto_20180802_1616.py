# Generated by Django 2.0.7 on 2018-08-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20180802_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='poster'),
        ),
    ]
