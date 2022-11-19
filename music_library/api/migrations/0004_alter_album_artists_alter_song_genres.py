# Generated by Django 4.1.2 on 2022-11-18 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_album_artists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artists',
            field=models.ManyToManyField(related_name='albums', to='api.artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='genres',
            field=models.ManyToManyField(related_name='songs', to='api.genre'),
        ),
    ]