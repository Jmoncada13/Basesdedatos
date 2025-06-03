# info de la materia: <ST0246> <Base-de-Datos>
#
# Estudiante(s): 
# Juan Sebastian Moncada, jsmoncadat@eafit.edu.co
# María Alejandra Martínez, mamaartineg@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya, emontoya@eafit.edu.co

# Diseño e Implementación de una base de datos para un Sistema de Gestión de Cursos (Nodo LMS)

<Este proyecto consiste en el diseño, modelado y desarrollo de una base de datos relacional para una plataforma de gestión de cursos en línea tipo LMS, llamada Nodo. La solución incluye desde el modelo entidad-relación hasta una aplicación web funcional desarrollada con Django y MySQL.>

## 1. ¿Qué aspectos se cumplieron o desarrollaron de la actividad propuesta por el profesor?

**Autenticación:**
- Login/Logout de usuarios usando email y contraseña.

**Funcionalidades para Administrador:**
- Matricular estudiantes en cursos.
- Asignar profesores a cursos.
- Ver cursos disponibles
- Reportes:
  - Listar cursos filtrados por fecha de inicio.
  - Ver detalles de un curso (profesor y estudiantes).
  - Listar usuarios filtrados por rol.

**Funcionalidades para Profesor y Estudiante:**
- Listar los cursos asignados.
- Ingresar a un curso y:
  - Listar alumnos del curso.
  - Listar materiales del curso.
  - Listar tareas del curso.
  - Listar y participar en foros.
- **Funciones exclusivas del profesor:**
  - Crear y subir materiales (simulados con URLs).
  - Crear foros.
- Salir de un curso y regresar al listado general.
- **Funciones exclusivas del estudiante:**
 - Entregar tareas

---

## 2. ¿Qué aspectos no se cumplieron?

- No se implementó la funcionalidad de envío de notificaciones al correo.
- No se gestionaron archivos reales (se simulan nombres).
- No se desplegó la aplicación en un servidor remoto o en AWS.

---

## 3. Descripción del ambiente de desarrollo y técnico

**Lenguaje principal:**  
Python 3.13.3

**Framework y herramientas utilizadas:**  
- Django 5.2.1  
- Django REST Framework 3.16.0  
- MySQL 8.0  
- Bootstrap 5.3 (para el frontend básico)

**Librerías y dependencias (versión exacta):**
