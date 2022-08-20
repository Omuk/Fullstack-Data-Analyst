# Generated by Django 4.0.6 on 2022-08-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('gal_pos', models.ImageField(default='default.jpg', upload_to='gal_poster')),
                ('pic', models.ImageField(default='default.jpg', upload_to='all_kids')),
            ],
        ),
    ]