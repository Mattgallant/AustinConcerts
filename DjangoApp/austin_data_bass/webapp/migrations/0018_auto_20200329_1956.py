# Generated by Django 3.0.4 on 2020-03-30 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_concerts_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='upcomingConcert',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
