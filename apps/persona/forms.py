from django import forms
from .models import Docente

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ('dni', 'nombre', 'apellido', 'cuil')
