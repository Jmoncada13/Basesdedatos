from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .decorators import role_required
from .forms import MatriculaForm
from django.contrib.auth.decorators import login_required
from .forms import AsignarProfesorForm
from .models import (
    Usuario, Curso, Interesa, Matricula, Material,
    Tarea, EntregaTarea, Foro, MensajeForo
)
from .serializers import (
    UsuarioSerializer, CursoSerializer, InteresaSerializer, MatriculaSerializer,
    MaterialSerializer, TareaSerializer, EntregaTareaSerializer,
    ForoSerializer, MensajeForoSerializer
)
from django.contrib.auth import logout

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class InteresaViewSet(viewsets.ModelViewSet):
    queryset = Interesa.objects.all()
    serializer_class = InteresaSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class EntregaTareaViewSet(viewsets.ModelViewSet):
    queryset = EntregaTarea.objects.all()
    serializer_class = EntregaTareaSerializer

class ForoViewSet(viewsets.ModelViewSet):
    queryset = Foro.objects.all()
    serializer_class = ForoSerializer

class MensajeForoViewSet(viewsets.ModelViewSet):
    queryset = MensajeForo.objects.all()
    serializer_class = MensajeForoSerializer

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        contraseña = request.POST['contraseña']
        try:
            usuario = Usuario.objects.get(email=email)
            if usuario.contraseña == contraseña:
                request.session['usuario_id'] = usuario.id_nodo
                request.session['rol'] = usuario.rol
                if usuario.rol == 'Administrador':
                    return redirect('admin_dashboard')
                elif usuario.rol == 'Profesor':
                    return redirect('profesor_dashboard')
                else:
                    return redirect('estudiante_dashboard')
            else:
                return render(request, 'cursos/login.html', {'error': 'Contraseña incorrecta'})
        except Usuario.DoesNotExist:
            return render(request, 'cursos/login.html', {'error': 'Usuario no encontrado'})
    return render(request, 'cursos/login.html')

def matricular_estudiante(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard') 
    else:
        form = MatriculaForm()
    return render(request, 'cursos/matricular_estudiante.html', {'form': form})

def cursos_y_estudiantes(request):
    cursos = Curso.objects.all()
    data = []

    for curso in cursos:
        matriculas = Matricula.objects.filter(id_curso=curso)

        estudiantes = Usuario.objects.filter(
            id_nodo__in=matriculas.values('id_nodo_estudiante'),
            rol='estudiante'
        )

        data.append({
            'curso': curso,
            'estudiantes': estudiantes
        })

    return render(request, 'cursos/cursos_y_estudiantes.html', {'cursos_data': data})

def listar_cursos_profesor(request):
    profesor_id = request.session.get('usuario_id')  # o el nombre de la clave que uses
    cursos = Curso.objects.filter(id_nodo_profesor_id=profesor_id)
    return render(request, 'profesor/listar_cursos.html', {'cursos': cursos})

def detalle_curso_profesor(request, curso_id):
    curso = get_object_or_404(Curso, id_curso=curso_id)
    return render(request, 'profesor/detalle_curso.html', {'curso': curso})

def listar_alumnos(request, curso_id):
    curso = get_object_or_404(Curso, id_curso=curso_id)
    matriculas = Matricula.objects.filter(id_curso=curso)
    estudiantes = [matricula.id_nodo_estudiante for matricula in matriculas]
    return render(request, 'profesor/listar_alumnos.html', {
        'curso': curso,
        'estudiantes': estudiantes
    })

@role_required(['Administrador'])
def asignar_profesor(request):
    if request.method == 'POST':
        form = AsignarProfesorForm(request.POST)
        if form.is_valid():
            curso = form.cleaned_data['curso']
            profesor = form.cleaned_data['profesor']
            curso.id_nodo_profesor = profesor
            curso.save()
            return redirect('admin_dashboard')
    else:
        form = AsignarProfesorForm()
    return render(request, 'cursos/asignar_profesor.html', {'form': form})

def cursos_disponibles(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/cursos_disponibles.html', {'cursos': cursos})

@role_required(['Administrador'])
def admin_dashboard(request):
    return render(request, 'cursos/admin_dashboard.html')

def home(request):
    return render(request, 'cursos/home.html')

@role_required(['Profesor'])
def profesor_dashboard(request):
    return render(request, 'profesor/profe_dashboard.html')

@role_required(['Estudiante'])
def estudiante_dashboard(request):
    return HttpResponse("Bienvenido al panel de estudiante")

def logout_view(request):
    request.session.flush()
    logout(request)
    response = redirect('login')
    response.delete_cookie('csrftoken')
    return response
