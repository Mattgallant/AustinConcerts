# Generated by Django 2.2.11 on 2020-03-29 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20200329_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concerts',
            name='imageURL',
        ),
    ]
