from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Usuario(models.Model):
    id_nodo = models.AutoField(primary_key=True)
    doc_identidad = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    nombre_completo = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('Otro', 'Otro'),
    ]
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)

    ROL_CHOICES = [
        ('Estudiante', 'Estudiante'),
        ('Profesor', 'Profesor'),
        ('Administrador', 'Administrador'),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)

    area_princ = models.CharField(max_length=100, blank=True, null=True)
    area_alt = models.CharField(max_length=100, blank=True, null=True)

    def clean(self):
        if self.rol != 'Profesor' and (self.area_princ or self.area_alt):
            raise ValidationError("Solo los profesores pueden tener área principal o alterna.")



class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_nodo_profesor = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True, related_name='cursos_asignados')
    categoria = models.CharField(max_length=100)
    url_contenido = models.URLField(max_length=255, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    anio = models.PositiveIntegerField()

    SEMESTRE_CHOICES = [
        ('1', 'Primer semestre'),
        ('2', 'Segundo semestre'),
    ]
    semestre = models.CharField(max_length=1, choices=SEMESTRE_CHOICES)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def clean(self):
        if not (2020 <= self.anio <= 2030):
            raise ValidationError("El año debe estar entre 2020 y 2030.")

   
