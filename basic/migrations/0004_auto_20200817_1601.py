# Generated by Django 3.0.8 on 2020-08-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_lissajouscurve_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lissajouscurve',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
