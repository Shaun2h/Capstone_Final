# Generated by Django 2.2.3 on 2019-07-30 03:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseclass',
            name='per_box',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='baseclass',
            name='pizzabox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='baseclass',
            name='sealed',
            field=models.BooleanField(default=False),
        ),
    ]