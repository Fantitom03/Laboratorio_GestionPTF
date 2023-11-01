from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import DocenteForm
from .models import Docente, Alumno, Asesor

# Vista para mostrar todos los docentes
def docente_list(request):
    docentes = Docente.objects.all()
    return render(request, 'docente_list.html', {'docentes': docentes})



# Vista para mostrar detalles de un docente específico
def docente_detail(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    return render(request, 'docente_detail.html', {'docente': docente})


# Vista para crear un nuevo docente
def docente_create(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            nuevo_docente = form.save(commit=True)
            messages.success(request, 'Se ha agregado correctamente el docente {}'.format(nuevo_docente))
            return redirect(reverse('persona:docente_list'))
    else:
        form = DocenteForm()
    return render(request, 'docente_create.html', {'form': form})


# Vista para actualizar un docente existente
def docente_edit(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            docente_editado = form.save(commit=True)
            docente = docente_editado
            docente.save()
            messages.success(request, 'Se ha actualizado correctamente el Docente')
            return redirect('persona:docente_detail', pk=docente.pk)
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'docente_edit.html', {'form': form, 'docente': docente})




# Vista para eliminar un docente existente
def docente_delete(request, pk):
    if request.method == 'POST':
        if 'id_docente' in request.POST:
            docente = get_object_or_404(Docente, pk=pk)
            nombre_persona = docente.nombre
            docente.delete()
            messages.success(request, 'Se ha eliminado exitosamente el Docente {}'.format(nombre_persona))
        else:
            messages.error(request, 'Debe indicar qué Docente desea eliminar')
    return redirect(reverse('persona:docente_list'))