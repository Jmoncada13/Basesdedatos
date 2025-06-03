# Info de la materia: ST0246 Base-de-Datos
#
# Estudiante(s): 
# Juan Sebastian Moncada, jsmoncadat@eafit.edu.co
# María Alejandra Martínez, mamaartineg@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya, emontoya@eafit.edu.co

# Diseño e Implementación de una base de datos para un Sistema de Gestión de Cursos (Nodo LMS)

Este proyecto consiste en el diseño, modelado e implementación de una base de datos relacional para una plataforma de gestión de cursos en línea tipo LMS, llamada **Nodo**. La solución abarca desde el modelo entidad-relación hasta una aplicación funcional desarrollada con Django y MySQL.

## 1. ¿Qué aspectos se cumplieron o desarrollaron de la actividad propuesta por el profesor?

**Autenticación:**
- Login/Logout de usuarios utilizando su email y contraseña.

**Funcionalidades para Administrador:**
- Matricular estudiantes en cursos.
- Asignar profesores a cursos.
- Ver el listado de cursos disponibles.
- Ver el listado de estudiantes inscritos a un curso.
- Generar reportes:
  - Listar cursos filtrados por fecha de inicio.
  - Ver detalles de un curso (profesor y estudiantes).
  - Listar usuarios filtrados por rol.

**Funcionalidades para Profesor y Estudiante:**
- Ver cursos asignados.
- Ingresar a un curso y:
  - Listar estudiantes del curso.
  - Listar materiales del curso.
  - Listar tareas asignadas.
  - Participar en foros.

**Funciones exclusivas del Profesor:**
- Crear y subir materiales (simulados con URLs).
- Crear foros.
- Crear tareas

**Funciones exclusivas del Estudiante:**
- Entregar tareas.

**Ambos roles pueden:**
- Salir de un curso y volver al listado general.

---

## 2. ¿Qué aspectos no se cumplieron?

- La interfaz visual puede mejorarse en términos de claridad y experiencia de usuario.
- La aplicación no fue desplegada en un servidor remoto o en la nube (ej. AWS).

---

## 3. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas

El sistema fue desarrollado bajo una arquitectura basada en el patrón **MVC (Modelo-Vista-Controlador)** proporcionado por Django, permitiendo una separación clara entre la lógica de negocio, la presentación y el acceso a los datos.

**Diseño y patrones utilizados:**
- Arquitectura modular con separación de roles (Administrador, Profesor, Estudiante).
- Acceso a base de datos mediante **Django ORM**, facilitando consultas seguras y legibles.
- Buenas prácticas implementadas:
  - Uso de variables de entorno (`.env`) para separar configuración sensible.
  - Decoradores personalizados para proteger rutas según el rol.
  - Organización del código en módulos funcionales (modelos, vistas, templates).
  - Serialización y consumo de datos con **Django REST Framework**.
- Autenticación basada en sesiones y control de acceso por rol.
- Vistas HTML con diseño limpio mediante **Bootstrap**, organizadas por tipo de usuario.

---

## 4. Descripción del ambiente de desarrollo y técnico

**Lenguaje principal:**  
- Python 3.13.3

**Frameworks y herramientas:**
- **Django 5.2.1:** Framework web que facilita el desarrollo rápido de aplicaciones con una arquitectura limpia.
- **Django REST Framework 3.16.0:** Extensión para crear APIs RESTful, con soporte para autenticación y serialización de datos.
- **MySQL 8.0:** Base de datos relacional utilizada para almacenar toda la información estructurada del sistema.
- **Bootstrap 5.3:** Framework frontend usado para mejorar el diseño de las vistas HTML.



**Librerías y dependencias (versión exacta):**
