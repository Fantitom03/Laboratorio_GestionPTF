from django import forms
from .models import EvaluacionPTF
class EvaluacionPTFForm(forms.ModelForm):
    class Meta:
        model = EvaluacionPTF
        fields = ['proyecto_TF', 'informe', 'fecha_evaluacion', 'estado', 'observaciones']
        widgets = {
            'fecha_evaluacion': forms.DateInput(attrs={'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }