# Generated by Django 3.0.8 on 2020-08-21 13:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0005_auto_20200820_2005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lissajouscurve',
            options={},
        ),
        migrations.AddField(
            model_name='lissajouscurve',
            name='upvotes',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]