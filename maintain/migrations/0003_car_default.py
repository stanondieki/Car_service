# Generated by Django 3.1.3 on 2020-11-17 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintain', '0002_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]
