# Generated by Django 3.0.4 on 2020-03-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20200327_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='latitude',
            field=models.DecimalField(decimal_places=13, default=0, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='longitude',
            field=models.DecimalField(decimal_places=13, default=0, max_digits=15),
            preserve_default=False,
        ),
    ]
