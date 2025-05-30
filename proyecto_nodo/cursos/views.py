from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .decorators import role_required
from django.db.models import Max
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import logout
from .forms import MatriculaForm, AsignarProfesorForm
from .models import (
    Usuario, Curso, Interesa, Matricula, Material,
    Tarea, EntregaTarea, Foro, MensajeForo
)
from .serializers import (
    UsuarioSerializer, CursoSerializer, InteresaSerializer, MatriculaSerializer,
    MaterialSerializer, TareaSerializer, EntregaTareaSerializer,
    ForoSerializer, MensajeForoSerializer
)

# ViewSets para API REST
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

# Autenticación y Home

def home(request):
    return render(request, 'cursos/home.html')

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

def logout_view(request):
    request.session.flush()
    logout(request)
    response = redirect('login')
    response.delete_cookie('csrftoken')
    return response

def registro_usuario(request):
    if request.method == 'POST':
        doc_identidad = request.POST.get('doc_identidad')
        email = request.POST.get('email')
        nombre_completo = request.POST.get('nombre_completo')
        contraseña = request.POST.get('contraseña')
        telefono = request.POST.get('telefono')
        genero = request.POST.get('genero')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Ya existe un usuario con este correo.')
        else:
            ultimo_id = Usuario.objects.aggregate(Max('id_nodo'))['id_nodo__max'] or 0
            nuevo_id = ultimo_id + 1

            usuario = Usuario(
                id_nodo=nuevo_id,
                doc_identidad=doc_identidad,
                email=email,
                nombre_completo=nombre_completo,
                contraseña=contraseña,
                telefono=telefono,
                genero=genero,
                rol='Estudiante',
            )
            usuario.save()
            return redirect('login')

    return render(request, 'cursos/registro.html')

# Paneles
@role_required(['Administrador'])
def admin_dashboard(request):
    return render(request, 'cursos/admin_dashboard.html')

@role_required(['Profesor'])
def profesor_dashboard(request):
    return render(request, 'profesor/profe_dashboard.html')

@role_required(['Estudiante'])
def estudiante_dashboard(request):
    return render(request, 'estudiantes/estudiante_dashboard.html')

# Vistas para Administrador
@role_required(['Administrador'])
def matricular_estudiante(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = MatriculaForm()
    return render(request, 'cursos/matricular_estudiante.html', {'form': form})

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

@role_required(['Administrador'])
def cursos_disponibles(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/cursos_disponibles.html', {'cursos': cursos})

@role_required(['Administrador'])
def cursos_y_estudiantes(request):
    cursos = Curso.objects.all()
    data = []
    for curso in cursos:
        matriculas = Matricula.objects.filter(id_curso=curso)
        estudiantes = Usuario.objects.filter(
            id_nodo__in=matriculas.values('id_nodo_estudiante'), rol='estudiante')
        data.append({'curso': curso, 'estudiantes': estudiantes})
    return render(request, 'cursos/cursos_y_estudiantes.html', {'cursos_data': data})

# Vistas para Profesor
@role_required(['Profesor'])
def listar_cursos_profesor(request):
    profesor_id = request.session.get('usuario_id')
    cursos = Curso.objects.filter(id_nodo_profesor_id=profesor_id)
    return render(request, 'profesor/listar_cursos.html', {'cursos': cursos})

@role_required(['Profesor'])
def detalle_curso_profesor(request, curso_id):
    curso = get_object_or_404(Curso, id_curso=curso_id)
    return render(request, 'profesor/detalle_curso.html', {'curso': curso})

@role_required(['Profesor'])
def listar_alumnos_profesor(request, curso_id):
    curso = get_object_or_404(Curso, id_curso=curso_id)
    matriculas = Matricula.objects.filter(id_curso=curso)
    estudiantes = [matricula.id_nodo_estudiante for matricula in matriculas]
    return render(request, 'profesor/listar_alumnos.html', {'curso': curso, 'estudiantes': estudiantes})

@role_required(['Profesor'])
def listar_materiales_profesor(request, curso_id):
    curso = get_object_or_404(Curso, id_curso=curso_id)
    materiales = Material.objects.filter(id_curso=curso)
    return render(request, 'profesor/listar_materiales.html', {'curso': curso, 'materiales': materiales})

@role_required(['Profesor'])
def crear_material(request, curso_id):
    curso = get_object_or_404(Curso, id_curso=curso_id)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        nombre_archivo = request.POST.get('nombre_archivo')
        if titulo and nombre_archivo:
            Material.objects.create(
                titulo=titulo, descripcion=descripcion, nombre_archivo=nombre_archivo, id_curso=curso)
            return redirect('listar_materiales_profesor', curso_id=curso.id_curso)
    return render(request, 'profesor/crear_material.html', {'curso': curso})

@role_required(['Profesor'])
def crear_foro(request, curso_id):
    curso = get_object_or_404(Curso, id_curso=curso_id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fecha_cierre = request.POST.get('fecha_cierre')
        if nombre:
            Foro.objects.create(
                id_curso=curso, nombre=nombre, descripcion=descripcion,
                fecha_cierre=fecha_cierre if fecha_cierre else None)
            return redirect('ver_foros_profesor', curso_id=curso.id_curso)
    return render(request, 'profesor/crear_foro.html', {'curso': curso})

@role_required(['Profesor'])
def ver_foros_profesor(request, curso_id):
    curso = get_object_or_404(Curso, id_curso=curso_id)
    foros = Foro.objects.filter(id_curso=curso)
    return render(request, 'profesor/foros.html', {'curso': curso, 'foros': foros})

@role_required(['Profesor'])
def ver_mensajes_foro_profesor(request, foro_id):
    foro = get_object_or_404(Foro, id_foro=foro_id)
    mensajes = MensajeForo.objects.filter(id_foro=foro, id_mensaje_padre=None).order_by('fecha_envio')
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        respuesta_a = request.POST.get('respuesta_a')
        usuario_id = request.session.get('usuario_id')
        if contenido and usuario_id:
            usuario = get_object_or_404(Usuario, id_nodo=usuario_id)
            MensajeForo.objects.create(
                id_foro=foro, id_nodo_usuario=usuario, contenido=contenido,
                fecha_envio=timezone.now(), id_mensaje_padre_id=respuesta_a or None)
            return redirect('ver_mensajes_foro_profesor', foro_id=foro.id_foro)
    return render(request, 'profesor/mensajes_foro.html', {'foro': foro, 'mensajes': mensajes})

@role_required(['Profesor'])
def ver_tareas_profesor(request, curso_id):
    curso = get_object_or_404(Curso, id_curso=curso_id)
    tareas = Tarea.objects.filter(id_curso=curso).order_by('fecha_entrega')
    return render(request, 'profesor/tareas.html', {'curso': curso, 'tareas': tareas})

@role_required(['Profesor'])
def crear_tarea(request, curso_id):
    curso = get_object_or_404(Curso, id_curso=curso_id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fecha_entrega = request.POST.get('fecha_entrega')
        archivo = request.POST.get('archivo')
        Tarea.objects.create(
            nombre=nombre, descripcion=descripcion,
            fecha_entrega=fecha_entrega, archivo=archivo,
            id_curso=curso, puntaje=0)
        return redirect('ver_tareas_profesor', curso_id=curso.id_curso)
    return render(request, 'profesor/crear_tarea.html', {'curso': curso})

# Vistas para Estudiante
@role_required(['Estudiante'])
def listar_cursos_estudiante(request):
    usuario_id = request.session.get('usuario_id')
    matriculas = Matricula.objects.filter(id_nodo_estudiante=usuario_id).select_related('id_curso')
    cursos = [m.id_curso for m in matriculas]
    return render(request, 'estudiantes/listar_cursos.html', {'cursos': cursos})

@role_required(['Estudiante'])
def detalle_curso_estudiante(request, curso_id):
    curso = get_object_or_404(Curso, id_curso=curso_id)
    usuario_id = request.session.get('usuario_id')
    esta_matriculado = Matricula.objects.filter(id_curso=curso, id_nodo_estudiante=usuario_id).exists()
    if not esta_matriculado:
        return HttpResponse("No estás matriculado en este curso.", status=403)
    return render(request, 'estudiantes/detalle_curso.html', {'curso': curso})

@role_required(['Estudiante'])
def listar_alumnos_estudiante(request, curso_id):
    curso = get_object_or_404(Curso, id_curso=curso_id)
    matriculas = Matricula.objects.filter(id_curso=curso)
    estudiantes = [matricula.id_nodo_estudiante for matricula in matriculas]
    return render(request, 'estudiantes/listar_alumnos.html', {'curso': curso, 'estudiantes': estudiantes})

@role_required(['Estudiante'])
def listar_materiales_estudiante(request, curso_id):
    curso = get_object_or_404(Curso, id_curso=curso_id)
    materiales = Material.objects.filter(id_curso=curso)
    return render(request, 'estudiantes/listar_materiales.html', {'curso': curso, 'materiales': materiales})

@role_required(['Estudiante'])
def ver_foros_estudiante(request, curso_id):
    curso = get_object_or_404(Curso, id_curso=curso_id)
    foros = Foro.objects.filter(id_curso=curso)
    return render(request, 'estudiantes/foros.html', {'curso': curso, 'foros': foros})

@role_required(['Estudiante'])
def ver_mensajes_foro_estudiante(request, foro_id):
    foro = get_object_or_404(Foro, id_foro=foro_id)
    mensajes = MensajeForo.objects.filter(id_foro=foro, id_mensaje_padre=None).order_by('fecha_envio')
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        respuesta_a = request.POST.get('respuesta_a')
        usuario_id = request.session.get('usuario_id')
        if contenido and usuario_id:
            usuario = get_object_or_404(Usuario, id_nodo=usuario_id)
            MensajeForo.objects.create(
                id_foro=foro, id_nodo_usuario=usuario, contenido=contenido,
                fecha_envio=timezone.now(), id_mensaje_padre_id=respuesta_a or None)
            return redirect('ver_mensajes_foro_estudiante', foro_id=foro.id_foro)
    return render(request, 'estudiantes/mensajes_foro.html', {'foro': foro, 'mensajes': mensajes})

@role_required(['Estudiante'])
def tareas(request, curso_id):
    curso = get_object_or_404(Curso, id_curso=curso_id)
    tareas = Tarea.objects.filter(id_curso=curso)
    estudiante_id = request.session.get('id_usuario') 
    entregas_dict = {}
    if estudiante_id:
        entregas = EntregaTarea.objects.filter(id_nodo_estudiante_id=estudiante_id, id_tarea__in=tareas)
        entregas_dict = {e.id_tarea.id_tarea: e.archivo_entregado for e in entregas}
    return render(request, 'estudiantes/tareas.html', {
        'curso': curso,
        'tareas': tareas,
        'entregas_dict': entregas_dict
    })

@role_required(['Estudiante'])
def entregar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id_tarea=tarea_id)
    if request.method == 'POST':
        archivo = request.POST.get('archivo_entregado')
        estudiante_id = request.POST.get('id_nodo_estudiante') 
        if archivo and estudiante_id:
            entrega, created = EntregaTarea.objects.get_or_create(
                id_tarea=tarea,
                id_nodo_estudiante_id=estudiante_id,
                defaults={'archivo_entregado': archivo}
            )
            if not created:
                entrega.archivo_entregado = archivo
                entrega.save()
            return redirect('tareas', curso_id=tarea.id_curso.id_curso)
    return render(request, 'estudiantes/entregar_tarea.html', {'tarea': tarea})


