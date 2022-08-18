# Generated by Django 4.0.6 on 2022-08-17 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_photos', '0002_photogallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryposter',
            name='pic',
        ),
        migrations.AddField(
            model_name='photogallery',
            name='albumpic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_photos.galleryposter'),
        ),
    ]
