from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, CursoViewSet
from . import views

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'cursos', CursoViewSet)

urlpatterns = [
    path('', include(router.urls)),  
    path('login/', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('profesor-dashboard/', views.profesor_dashboard, name='profesor_dashboard'),
    path('estudiante-dashboard/', views.estudiante_dashboard, name='estudiante_dashboard'),
]
