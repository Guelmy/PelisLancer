# Generated by Django 2.0.2 on 2018-02-23 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20180223_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('apellido', models.CharField(max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='peliculas',
            name='Usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.usuario'),
        ),
    ]
