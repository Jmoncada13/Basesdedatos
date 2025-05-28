from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('profesor-dashboard/', views.profesor_dashboard, name='profesor_dashboard'),
    path('estudiante-dashboard/', views.estudiante_dashboard, name='estudiante_dashboard'),
    path('matricular/', views.matricular_estudiante, name='matricular_estudiante')
,
]
