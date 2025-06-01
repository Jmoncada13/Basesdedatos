from django.urls import path
from . import views

urlpatterns = [
    # Home y autenticación
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_usuario, name='registro_usuario'),

    # Paneles por rol
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('profesor-dashboard/', views.profesor_dashboard, name='profesor_dashboard'),
    path('estudiante-dashboard/', views.estudiante_dashboard, name='estudiante_dashboard'),

    # Admin
    path('matricular/', views.matricular_estudiante, name='matricular_estudiante'),
    path('asignar-profesor/', views.asignar_profesor, name='asignar_profesor'),
    path('cursos-disponibles/', views.cursos_disponibles, name='cursos_disponibles'),
    path('cursos-disponibles/<int:curso_id>/estudiantes/', views.estudiantes_curso_admin, name='estudiantes_curso_admin'),
    path('cursos-con-estudiantes/', views.cursos_y_estudiantes, name='cursos_y_estudiantes'),

    # Profesor
    path('profesor/cursos/', views.listar_cursos_profesor, name='listar_cursos_profesor'),
    path('profesor/curso/<int:curso_id>/', views.detalle_curso_profesor, name='detalle_curso_profesor'),
    path('profesor/curso/<int:curso_id>/alumnos/', views.listar_alumnos_profesor, name='listar_alumnos_profesor'),
    path('profesor/curso/<int:curso_id>/materiales/', views.listar_materiales_profesor, name='listar_materiales_profesor'),
    path('profesor/curso/<int:curso_id>/materiales/nuevo/', views.crear_material, name='crear_material'),
    path('profesor/curso/<int:curso_id>/foros/', views.ver_foros_profesor, name='ver_foros_profesor'),
    path('profesor/foro/<int:foro_id>/mensajes/', views.ver_mensajes_foro_profesor, name='ver_mensajes_foro_profesor'),
    path('curso/<int:curso_id>/crear-foro/', views.crear_foro, name='crear_foro'),
    path('profesor/curso/<int:curso_id>/tareas/', views.ver_tareas_profesor, name='ver_tareas_profesor'),
    path('profesor/curso/<int:curso_id>/tareas/nueva/', views.crear_tarea, name='crear_tarea'),

    # Estudiante
    path('estudiantes/cursos/', views.listar_cursos_estudiante, name='listar_cursos_estudiante'),
    path('estudiantes/curso/<int:curso_id>/', views.detalle_curso_estudiante, name='detalle_curso_estudiante'),
    path('estudiantes/curso/<int:curso_id>/alumnos/', views.listar_alumnos_estudiante, name='listar_alumnos_estudiante'),
    path('estudiantes/curso/<int:curso_id>/materiales/', views.listar_materiales_estudiante, name='listar_materiales_estudiante'),
    path('estudiantes/curso/<int:curso_id>/foros/', views.ver_foros_estudiante, name='ver_foros_estudiante'),
    path('estudiantes/foro/<int:foro_id>/mensajes/', views.ver_mensajes_foro_estudiante, name='ver_mensajes_foro_estudiante'),
    path('estudiantes/curso/<int:curso_id>/tareas/', views.tareas, name='tareas'),
    path('estudiantes/tarea/<int:tarea_id>/entrega/', views.entregar_tarea, name='entregar_tarea'),
]
