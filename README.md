# Proyecto Django - Web page company

## Descripción
Proyecto enfocado en el desarrollo de una pagina web utilizando
la  herramienta de Django 5.

## Tecnologías utilizadas
- Django 
- Python  
- SQLite 
- HTML, CSS

## Requisitos previos
Antes de ejecutar el proyecto, asegúrate de tener instalado:
- Python (versión recomendada: 3.12)  
- Django (versión recomendada: 5)  
- vitualvenv 20.26.3 

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/hcruz93/django-course.git
   ```
2. Accede al directorio del proyecto:
   ```bash
   cd django-course
   ```
3. Crea un entorno virtual y actívalo:
   ```bash
   virtualenv -p ruta-python-python.exe venv 
   venv\Scripts\activate # Activar el ambiente en Windows
   deactuvate # comando para desactivar el ambiente vitual

   ```
4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt 
   ```
5. Configura el archivo `.env` (si se usa configuración con variables de entorno).  
6. Aplica las migraciones de la base de datos:
   ```bash
   python manage.py migrate
   python manage.py makemigrations # si agregas nuevas cosas
   ```
7. Crea un superusuario:
   ```bash
   python manage.py createsuperuser
   ```
8. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Uso
Accede al proyecto en el navegador a través de `http://127.0.0.1:8000/`.  

## Autor  
Este proyecto fue desarrollado por Humberto Cruz, basado en el curso Django 5 - Build a Complete Website from Scratch to Deploy
 de Azzam Makki.

