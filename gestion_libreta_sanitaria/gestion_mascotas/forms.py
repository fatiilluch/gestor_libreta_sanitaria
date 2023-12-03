from django import forms
from django.forms import DateInput
from .models import Vacune

class VacuneForm(forms.ModelForm):
    class Meta:
        model = Vacune
        fields = ['nombre', 'dia_aplicacion', 'proxima_fecha']
        widgets = {
            'dia_aplicacion': DateInput(attrs={'type': 'date'}),
            'proxima_fecha': DateInput(attrs={'type': 'date'})
        }
