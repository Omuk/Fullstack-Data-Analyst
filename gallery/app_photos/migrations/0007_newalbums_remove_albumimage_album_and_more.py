# Generated by Django 4.0.6 on 2022-08-18 03:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_photos', '0006_album_albumimage_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewAlbums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('pictur', models.ImageField(default='default.jpg', upload_to='gal_poster')),
                ('alt', models.CharField(default=uuid.uuid4, max_length=255)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_photos.galleryposter')),
            ],
        ),
        migrations.RemoveField(
            model_name='albumimage',
            name='album',
        ),
        migrations.RemoveField(
            model_name='photogallery',
            name='albumpic',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='post',
        ),
        migrations.RemoveField(
            model_name='rafikigallery',
            name='albumpi',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='AlbumImage',
        ),
        migrations.DeleteModel(
            name='PhotoGallery',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
        migrations.DeleteModel(
            name='RafikiGallery',
        ),
    ]
