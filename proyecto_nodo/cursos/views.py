from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MatriculaForm
from django.contrib.auth.decorators import login_required
from .models import (
    Usuario, Curso, Interesa, Matricula, Material,
    Tarea, EntregaTarea, Foro, MensajeForo
)
from .serializers import (
    UsuarioSerializer, CursoSerializer, InteresaSerializer, MatriculaSerializer,
    MaterialSerializer, TareaSerializer, EntregaTareaSerializer,
    ForoSerializer, MensajeForoSerializer
)

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

def admin_dashboard(request):
    return render(request, 'cursos/admin_dashboard.html')

def home(request):
    return render(request, 'cursos/home.html')

def profesor_dashboard(request):
    return HttpResponse("Bienvenido al panel de profesor")

def estudiante_dashboard(request):
    return HttpResponse("Bienvenido al panel de estudiante")
