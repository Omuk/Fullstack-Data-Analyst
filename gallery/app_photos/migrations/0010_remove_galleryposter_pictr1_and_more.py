# Generated by Django 4.0.6 on 2022-08-18 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_photos', '0009_galleryposter_alt_galleryposter_pictr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryposter',
            name='pictr1',
        ),
        migrations.RemoveField(
            model_name='galleryposter',
            name='pictr2',
        ),
        migrations.RemoveField(
            model_name='galleryposter',
            name='pictr3',
        ),
        migrations.RemoveField(
            model_name='galleryposter',
            name='pictr4',
        ),
    ]
