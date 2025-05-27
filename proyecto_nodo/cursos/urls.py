from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet, CursoViewSet, InteresaViewSet, MatriculaViewSet,
    MaterialViewSet, TareaViewSet, EntregaTareaViewSet,
    ForoViewSet, MensajeForoViewSet,
    login_view, admin_dashboard, profesor_dashboard, estudiante_dashboard
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'interesa', InteresaViewSet)
router.register(r'matriculas', MatriculaViewSet)
router.register(r'materiales', MaterialViewSet)
router.register(r'tareas', TareaViewSet)
router.register(r'entregas', EntregaTareaViewSet)
router.register(r'foros', ForoViewSet)
router.register(r'mensajes-foro', MensajeForoViewSet)

urlpatterns = [
    path('', include(router.urls)),  
    path('login/', login_view, name='login'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('profesor-dashboard/', profesor_dashboard, name='profesor_dashboard'),
    path('estudiante-dashboard/', estudiante_dashboard, name='estudiante_dashboard'),
]
