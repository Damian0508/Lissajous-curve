from django import forms
from .models import LissajousCurve


class CurveParamaterForm(forms.ModelForm):
    x_frequency = forms.IntegerField(min_value=1, max_value=2000)
    y_frequency = forms.IntegerField(min_value=1, max_value=2000)
    phase = forms.IntegerField(min_value=0, max_value=360)
    simulation_time = forms.FloatField(min_value=0.1, max_value=10)
    image = forms.CharField(widget= forms.HiddenInput(), required=False)
    class Meta:
        model = LissajousCurve
        exclude = ['date']

