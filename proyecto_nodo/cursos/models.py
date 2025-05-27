from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Usuario(models.Model):
    id_nodo = models.AutoField(primary_key=True)
    doc_identidad = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    nombre_completo = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    GENERO_CHOICES = [('M', 'Masculino'), ('F', 'Femenino'), ('Otro', 'Otro')]
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)

    ROL_CHOICES = [('Estudiante', 'Estudiante'), ('Profesor', 'Profesor'), ('Administrador', 'Administrador')]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)

    area_princ = models.CharField(max_length=100, blank=True, null=True)
    area_alt = models.CharField(max_length=100, blank=True, null=True)

    def clean(self):
        if self.rol != 'Profesor' and (self.area_princ or self.area_alt):
            raise ValidationError("Solo los profesores pueden tener área principal o alterna.")


# ------------------ CURSO ------------------
class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_nodo_profesor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='cursos_asignados')
    categoria = models.CharField(max_length=100)
    url_contenido = models.URLField(max_length=255, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    anio = models.PositiveIntegerField()
    SEMESTRE_CHOICES = [('1', 'Primer semestre'), ('2', 'Segundo semestre')]
    semestre = models.CharField(max_length=1, choices=SEMESTRE_CHOICES)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def clean(self):
        if not (2020 <= self.anio <= 2030):
            raise ValidationError("El año debe estar entre 2020 y 2030.")


class Interesa(models.Model):
    id_nodo_profesor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'Profesor'})
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('id_nodo_profesor', 'id_curso')


class Matricula(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    id_nodo_estudiante = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'Estudiante'})
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    comprobante_pago = models.CharField(max_length=100)

    class Meta:
        unique_together = ('id_nodo_estudiante', 'id_curso')


class Material(models.Model):
    id_material = models.AutoField(primary_key=True)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    nombre_archivo = models.CharField(max_length=100)

class Tarea(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    puntaje = models.DecimalField(max_digits=3, decimal_places=2)
    archivo = models.CharField(max_length=100)

    def clean(self):
        if not (0.0 <= self.puntaje <= 5.0):
            raise ValidationError("El puntaje debe estar entre 0.00 y 5.00")


class EntregaTarea(models.Model):
    id_tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    id_nodo_estudiante = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'Estudiante'})
    puntaje = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    archivo_entregado = models.CharField(max_length=100)
    fecha_entrega = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('id_tarea', 'id_nodo_estudiante')


class Foro(models.Model):
    id_foro = models.AutoField(primary_key=True)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateField(blank=True, null=True)


class MensajeForo(models.Model):
    id_mensaje = models.AutoField(primary_key=True)
    id_foro = models.ForeignKey(Foro, on_delete=models.CASCADE)
    id_nodo_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_mensaje_padre = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
   
