# Generated by Django 3.2.9 on 2021-11-14 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coolkats_app', '0004_auto_20211114_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletime',
            name='endTime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='availabletime',
            name='startTime',
            field=models.DateTimeField(null=True),
        ),
    ]
