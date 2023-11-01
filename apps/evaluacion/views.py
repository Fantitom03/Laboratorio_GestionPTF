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


def evaluacionPTF_create(request):

    if request.method == 'POST':
        form = EvaluacionPTFForm(request.POST)
        if form.is_valid():
            nueva_evaluacion = form.save(commit=False)
            nueva_evaluacion.clean()
            nueva_evaluacion.save()
            messages.success(request, 'Se ha agregado correctamente la evaluación')
            return redirect(reverse('evaluacion:evaluacionPTF_list'))
    else:
        form = EvaluacionPTFForm()  # Pasa el proyecto como valor inicial

    return render(request, 'evaluacionPTF_create.html', {'form': form})

def evaluacionPTF_edit (request, pk):
    evaluacion = get_object_or_404(EvaluacionPTF, pk=pk)
    if request.method == 'POST':
        form = EvaluacionPTFForm(request.POST, instance=evaluacion)
        if form.is_valid():
            evaluacion_editada = form.save(commit=True)
            evaluacion = evaluacion_editada
            evaluacion.save()
            messages.success(request, 'Se ha actualizado correctamente la evaluación')
            return redirect('evaluacion:evaluacionPTF_detail', pk=evaluacion.pk)
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = EvaluacionPTFForm(instance=evaluacion)
    return render(request, 'evaluacionPTF_edit.html', {'form': form, 'evaluacion': evaluacion})

def evaluacionPTF_delete(request, pk):
    if request.method == 'POST':
        if 'id_evaluacion' in request.POST:
            evaluacion = get_object_or_404(EvaluacionPTF, pk=pk)
            evaluacion.delete()
            messages.success(request, 'Se ha eliminado exitosamente la evaluacion')
        else:
            messages.error(request, 'Debe indicar qué evaluació desea eliminar')
    return redirect(reverse('evaluacion:evaluacionPTF_list'))

