# Generated by Django 2.0.2 on 2018-02-23 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_delete_usuarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='peliculas',
            name='create_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='imagen',
            field=models.ImageField(null=True, upload_to='pelis-image'),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='update_at',
            field=models.DateTimeField(null=True),
        ),
    ]
