# Generated by Django 2.2.11 on 2020-03-25 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('spotifyID', models.CharField(max_length=30)),
                ('imageLink', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=500)),
                ('genres', models.CharField(max_length=50)),
                ('popularity', models.IntegerField()),
                ('followers', models.IntegerField()),
                ('topTracks', models.CharField(max_length=50)),
            ],
        ),
    ]