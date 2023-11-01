from django import forms
from .models import EvaluacionPTF
from apps.proyectotf.models import Proyecto_TF
class EvaluacionPTFForm(forms.ModelForm):
    proyecto_tf = forms.ModelChoiceField(
        queryset=Proyecto_TF.objects.all(),  # Incluye todos los proyectos
        empty_label="Selecciona un proyecto",  # Opción predeterminada en el campo
    )

    class Meta:
        model = EvaluacionPTF
        fields = ['proyecto_tf', 'fecha_evaluacion', 'estado', 'observaciones']
        #falta el informe lpm
        widgets = {
            'fecha_evaluacion': forms.DateInput(attrs={'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza el queryset si es necesario
        # self.fields['proyecto_tf'].queryset = Proyecto_TF.objects.filter(tu_filtro_personalizado)