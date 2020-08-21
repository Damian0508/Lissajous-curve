from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class LissajousCurve(models.Model):
    x_frequency = models.IntegerField(
        validators=[
            MaxValueValidator(2000),
            MinValueValidator(1)
        ])
    y_frequency = models.IntegerField(
        validators=[
            MaxValueValidator(2000),
            MinValueValidator(1)
        ])
    phase = models.IntegerField(
        validators=[
            MaxValueValidator(360),
            MinValueValidator(0)
        ])
    simulation_time = models.FloatField(validators=[
            MaxValueValidator(10),
            MinValueValidator(0.1)
        ])
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to ='plots', default='default.jpg')

    class Meta:
        ordering = ['-date']