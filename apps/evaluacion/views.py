from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Proyecto_TF, EvaluacionPTF
from .forms import EvaluacionPTFForm
from django.contrib import messages

def evaluacionPTF_list(request):
    evaluaciones = EvaluacionPTF.objects.all()
    return render(request, 'evaluacionPTF_list.html', {'evaluaciones': evaluaciones})

def evaluacionPTF_detail(request, pk):
    evaluacion = get_object_or_404(EvaluacionPTF, pk=pk)
    return render(request, 'evaluacionPTF_detail.html', {'evaluacion': evaluacion})


def evaluacionPTF_create (request):
    if request.method == 'POST':
        form = EvaluacionPTFForm(request.POST)
        if form.is_valid():
            nueva_evaluacion = form.save(commit=True)
            nueva_evaluacion.clean()
            nueva_evaluacion.save()
            messages.success(request, 'Se ha agregado correctemente la evaluacion')
            return redirect(reverse('evaluacion:evaluacionPTF_list'))
        else:
            form = EvaluacionPTFForm()
        return render(request, 'evaluacionPTF_create.html',)

