from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('profesor-dashboard/', views.profesor_dashboard, name='profesor_dashboard'),
    path('estudiante-dashboard/', views.estudiante_dashboard, name='estudiante_dashboard'),
    path('matricular/', views.matricular_estudiante, name='matricular_estudiante'),
    path('asignar-profesor/', views.asignar_profesor, name='asignar_profesor'),
    path('cursos-disponibles/', views.cursos_disponibles, name='cursos_disponibles'),
    path('cursos-con-estudiantes/', views.cursos_y_estudiantes, name='cursos_y_estudiantes'),
    path('profesor/cursos/', views.listar_cursos_profesor, name='listar_cursos_profesor'),
    path('profesor/curso/<int:curso_id>/', views.detalle_curso_profesor, name='detalle_curso_profesor'),
    path('profesor/curso/<int:curso_id>/alumnos/', views.listar_alumnos, name='listar_alumnos'),
    path('profesor/curso/<int:curso_id>/materiales/', views.listar_materiales, name='listar_materiales'),
    path('profesor/curso/<int:curso_id>/foros/', views.ver_foros, name='ver_foros'),
    path('profesor/foro/<int:foro_id>/mensajes/', views.ver_mensajes_foro, name='ver_mensajes_foro'),
    path('curso/<int:curso_id>/crear-foro/', views.crear_foro, name='crear_foro'),
    path('profesor/curso/<int:curso_id>/tareas/', views.ver_tareas, name='ver_tareas'),
    path('profesor/curso/<int:curso_id>/tareas/nueva/', views.crear_tarea, name='crear_tarea'),
    path('profesor/curso/<int:curso_id>/materiales/nuevo/', views.crear_material, name='crear_material'),
    path('profesor/curso/<int:curso_id>/materiales/nuevo/', views.crear_material, name='crear_material'),
    path('logout/', views.logout_view, name='logout'),
]
