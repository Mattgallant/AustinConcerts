# Generated by Django 3.0.4 on 2020-03-30 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0022_merge_20200329_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='upcomingConcert',
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=105),
        ),
    ]