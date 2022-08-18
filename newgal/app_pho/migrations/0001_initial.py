# Generated by Django 4.0.6 on 2022-08-18 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.FileField(default='default.jpg', upload_to='album_prof')),
            ],
        ),
        migrations.CreateModel(
            name='AlbumPics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='pics')),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_pho.album')),
            ],
        ),
    ]
