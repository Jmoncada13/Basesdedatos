# ST0246 Base-de-Datos

## Estudiante(s): 
- Juan Sebastian Moncada, jsmoncadat@eafit.edu.co
- María Alejandra Martínez, mamaartineg@eafit.edu.co

## Profesor:
- Edwin Nelson Montoya, emontoya@eafit.edu.co

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

El sistema fue desarrollado bajo una arquitectura basada en el patrón **MTV (Model-Template-View)** proporcionado por Django, permitiendo una separación clara entre la lógica de negocio, la presentación y el acceso a los datos.

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
- asgiref==3.8.1
- djangorestframework==3.16.0
- mysqlclient==2.2.7
- python-decouple==3.8
- sqlparse==0.5.3
- tzdata==2025.2

**Compilar y ejecutar**
- Clonar el repositorio:
  - git clone https://github.com/Jmoncada13/Basesdedatos.git
  - cd proyecto_nodo
- Crear entorno virtual e instalar dependencias:
  - python -m venv venv
  - source venv/bin/activate  # o venv\Scripts\activate en Windows
  - pip install -r requirements.txt
- Configurar variables de entorno en un archivo .env:
  - DjangoSettings
    - DEBUG=True
    - SECRET_KEY=django-insecure-...
    - ALLOWED_HOSTS=127.0.0.1,localhost

  - MySQL
    - DB_NAME=nombre_DB
    - DB_USER=usuario_mysql
    - DB_PASSWORD=contraseña_mysql
    - DB_HOST=localhost
    - DB_PORT=3306
 
- Aplicar migraciones y lanzar servidor:
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py runserver
 
- Detalles del desarrollo
  - Se desarrolló una única app llamada cursos, que agrupa modelos, vistas, URLs y formularios.
  - Se utilizaron decoradores personalizados para proteger vistas según el rol (@role_required).
  - El control de acceso se maneja mediante sesiones y verificación del id_usuario y rol.
  - Se implementó un sistema de plantillas HTML organizadas por tipo de usuario (estudiantes, profesor, admin).

- Detalles técnicos
  - El archivo settings.py utiliza python-decouple para cargar variables del archivo .env.
  - Conexión a MySQL mediante la librería mysqlclient.
  - serializers.py expone datos a través de la API REST.
  - Las rutas están organizadas en urls.py (vistas generales) y api_urls.py (API REST).

- Organización


![image](https://github.com/user-attachments/assets/d0e48f85-2f4e-4b78-968b-49a278d55c7d)

- Cómo ejecutar la aplicación
  - python manage.py runserver
  - Esto levanta el servidor en el puerto 8000 por defecto, accesible desde el navegador en http://127.0.0.1:8000.

## Guía para el usuario
- Registro e inicio de sesión:
  - El usuario se registra con sus datos personales.
  - Inicia sesión usando su email y contraseña.

- Si es estudiante:

  - Visualiza sus cursos asignados.

  - Accede al detalle de cada curso para:

  - Descargar materiales.

  - Ver tareas y entregarlas.

  - Participar en foros.

- Si es profesor:

  - Visualiza los cursos que le han sido asignados.

  - Puede:

    - Subir materiales (URL simulada).

    - Crear tareas.

    - Crear foros y responder mensajes.

- Si es administrador:

  - Matricula estudiantes en cursos.

  - Asigna profesores a cursos.

  - Visualiza reportes por fecha o por rol.

## REFERENCIAS
  - https://www.youtube.com/watch?v=nGIg40xs9e4
  - https://www.django-rest-framework.org/
  - https://docs.djangoproject.com/en/5.2/
  - https://docs.djangoproject.com/es/5.2/faq/models/
  - https://getbootstrap.com/docs/5.3/getting-started/introduction/


