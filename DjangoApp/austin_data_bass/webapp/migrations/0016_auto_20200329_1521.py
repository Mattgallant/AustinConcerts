# Generated by Django 3.0.4 on 2020-03-29 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_artist_upcomingconcert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='upcomingConcert',
            field=models.CharField(max_length=200),
        ),
    ]