# Generated by Django 2.0.2 on 2018-02-23 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20180223_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peliculas',
            old_name='price',
            new_name='precio',
        ),
    ]