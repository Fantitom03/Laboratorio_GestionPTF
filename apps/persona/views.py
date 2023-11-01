from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import DocenteForm, AlumnoForm, AsesorForm
from .models import Docente, Alumno, Asesor, Persona
from django.contrib.auth import authenticate, login, logout

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
            docente_id = request.POST['id_docente']
            docente = get_object_or_404(Docente, pk=docente_id)
            nombre_persona = docente.nombre
            docente.delete()
            messages.success(request, 'Se ha eliminado exitosamente el Docente {}'.format(nombre_persona))
        else:
            messages.error(request, 'Debe indicar qué Docente desea eliminar')
    return redirect(reverse('persona:docente_list'))




#--------
#ALUMNOS
#-------

def alumno_list(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumno_list.html', {'alumnos': alumnos})

def alumno_detail(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'alumno_detail.html', {'alumno': alumno})


# Vista para crear un nuevo alumno
def alumno_create(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            nuevo_alumno = form.save(commit=True)
            messages.success(request, 'Se ha agregado correctamente el Alumno {}'.format(nuevo_alumno))
            return redirect(reverse('persona:alumno_list'))
    else:
        form = AlumnoForm()
    return render(request, 'alumno_create.html', {'form': form})


# Vista para actualizar un alumno existente
def alumno_edit(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            alumno_editado = form.save(commit=True)
            alumno = alumno_editado
            alumno.save()
            messages.success(request, 'Se ha actualizado correctamente el Alumno')
            return redirect('persona:alumno_detail', pk=alumno.pk)
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumno_edit.html', {'form': form, 'alumno': alumno})




# Vista para eliminar un alumno existente
def alumno_delete(request, pk):
    if request.method == 'POST':
        if 'id_alumno' in request.POST:
            alumno_id = request.POST['id_alumno']
            alumno = get_object_or_404(Alumno, pk=alumno_id)
            nombre_persona = alumno.nombre
            alumno.delete()
            messages.success(request, 'Se ha eliminado exitosamente el Alumno {}'.format(nombre_persona))
        else:
            messages.error(request, 'Debe indicar qué Alumno desea eliminar')
    return redirect(reverse('persona:alumno_list'))



#-----------
#-----------
#ASESORES
#-----------
#-----------


def asesor_list(request):
    asesores = Asesor.objects.all()
    return render(request, 'asesor_list.html', {'asesores': asesores})

def asesor_detail(request, pk):
    asesor = get_object_or_404(Asesor, pk=pk)
    return render(request, 'asesor_detail.html', {'asesor': asesor})


# Vista para crear un nuevo asesor
def asesor_create(request):
    if request.method == 'POST':
        form = AsesorForm(request.POST)
        if form.is_valid():
            nuevo_asesor = form.save(commit=True)
            messages.success(request, 'Se ha agregado correctamente el Asesor {}'.format(nuevo_asesor))
            return redirect(reverse('persona:asesor_list'))
    else:
        form = AsesorForm()
    return render(request, 'asesor_create.html', {'form': form})


# Vista para actualizar un asesor existente
def asesor_edit(request, pk):
    asesor = get_object_or_404(Asesor, pk=pk)
    if request.method == 'POST':
        form = AsesorForm(request.POST, instance=asesor)
        if form.is_valid():
            asesor_editado = form.save(commit=True)
            asesor = asesor_editado
            asesor.save()
            messages.success(request, 'Se ha actualizado correctamente el Asesor')
            return redirect('persona:asesor_detail', pk=asesor.pk)
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = AsesorForm(instance=asesor)
    return render(request, 'asesor_edit.html', {'form': form, 'asesor': asesor})




# Vista para eliminar un asesor existente
def asesor_delete(request, pk):
    if request.method == 'POST':
        if 'id_asesor' in request.POST:
            asesor_id = request.POST['id_asesor']
            asesor = get_object_or_404(Asesor, pk=asesor_id)
            nombre_persona = asesor.nombre
            asesor.delete()
            messages.success(request, 'Se ha eliminado exitosamente el Asesor {}'.format(nombre_persona))
        else:
            messages.error(request, 'Debe indicar qué Asesor desea eliminar')
    return redirect(reverse('persona:asesor_list'))

#--------------------------------
#--------------------------------
#USER VIEWS
#--------------------------------
#--------------------------------

def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse("persona:login"))
    return render(request, "persona/usuario.html")



def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("persona:index"))
        else:
            return render(request, "persona/login.html", { "msj": "Credencialesincorrectas" })
    return render(request, "persona/login.html")



def logout_view(request):
    logout(request)
    return render(request, "persona/login.html", { "msj": "Deslogueado" })






































