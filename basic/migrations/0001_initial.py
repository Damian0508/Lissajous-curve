# Generated by Django 3.0.8 on 2020-08-08 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LissajousCurve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_frequency', models.IntegerField()),
                ('y_frequency', models.IntegerField()),
                ('phase', models.IntegerField()),
                ('simulation_time', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
