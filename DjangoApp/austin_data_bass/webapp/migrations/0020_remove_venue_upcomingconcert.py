# Generated by Django 3.0.4 on 2020-03-30 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0019_auto_20200330_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='upcomingConcert',
        ),
    ]