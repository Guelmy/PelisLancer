# Generated by Django 2.0.2 on 2018-02-23 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peliculas',
            name='cuerpo',
        ),
        migrations.AddField(
            model_name='peliculas',
            name='genero',
            field=models.TextField(default=5, max_length=100),
            preserve_default=False,
        ),
    ]
