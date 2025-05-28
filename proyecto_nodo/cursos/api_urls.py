from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet, CursoViewSet, InteresaViewSet, MatriculaViewSet,
    MaterialViewSet, TareaViewSet, EntregaTareaViewSet,
    ForoViewSet, MensajeForoViewSet
)
from django.urls import path

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

urlpatterns = router.urls 

