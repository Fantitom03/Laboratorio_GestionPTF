from django.shortcuts import render, get_object_or_404, redirect
from .forms import DocenteForm
from .models import Docente, Alumno, Asesor, Persona

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
            form.save()
            return redirect('docente_list')
    else:
        form = DocenteForm()
    return render(request, 'docente_create.html', {'form': form})


# Vista para actualizar un docente existente
def docente_update(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    # Lógica para procesar el formulario de actualización de docente
    # ...
    return render(request, 'docente_form.html', {'docente': docente})


# Vista para eliminar un docente existente
def docente_delete(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    docente.delete()
    # Redirigir a la lista de docentes después de la eliminación
    return redirect('docente_list')