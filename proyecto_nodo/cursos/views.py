
from rest_framework import viewsets
from .models import Usuario, Curso
from .serializers import UsuarioSerializer, CursoSerializer
from django.shortcuts import render, redirect
from django.http import HttpResponse


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        contraseña = request.POST['contraseña']
        try:
            usuario = Usuario.objects.get(email=email)
            if usuario.contraseña == contraseña:
                request.session['usuario_id'] = usuario.id_nodo
                request.session['rol'] = usuario.rol
                # Redirigir según el rol
                if usuario.rol == 'Administrador':
                    return redirect('admin_dashboard')
                elif usuario.rol == 'Profesor':
                    return redirect('profesor_dashboard')
                else:
                    return redirect('estudiante_dashboard')
            else:
                return render(request, 'login.html', {'error': 'Contraseña incorrecta'})
        except Usuario.DoesNotExist:
            return render(request, 'login.html', {'error': 'Usuario no encontrado'})
    return render(request, 'login.html')

def admin_dashboard(request):
    return HttpResponse("Bienvenido al panel de administrador")

def profesor_dashboard(request):
    return HttpResponse("Bienvenido al panel de profesor")

def estudiante_dashboard(request):
    return HttpResponse("Bienvenido al panel de estudiante")
