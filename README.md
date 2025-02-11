# alfredo-fernandez-reclamos

Sistema de gestión de reclamos para Alfredo Fernandez. Esta aplicación permite administrar y dar seguimiento a los reclamos de clientes de manera eficiente.

## Características principales

- Registro y seguimiento de reclamos
- Panel de administración intuitivo
- Gestión de estados de reclamos

## Instalación
- Clona el repositorio: `git clone https://github.com/tu-usuario/alfredo-fernandez-reclamos.git`
- Navega al directorio del proyecto: `cd alfredo-fernandez-reclamos`
- Crea un entorno virtual: `python -m venv venv`
- Activa el entorno virtual: `source venv/bin/activate` (en Linux/Mac) o `venv\Scripts\activate` (en Windows)
- Instala las dependencias: `pip install -r requirements.txt`
- Aplica las migraciones: `python manage.py migrate`
- Crea un superusuario: `python manage.py createsuperuser`
- Inicia el servidor de desarrollo: `python manage.py runserver`
- Accede a la aplicación en tu navegador: `http://127.0.0.1:8000/admin` para probar el modulo de administracion
- Accede a la aplicación en tu navegador: `http://127.0.0.1:8000` para ingresar a la pagina principal.
- Accede a la aplicación en tu navegador: `http://127.0.0.1:8000/reclamo-crear/` para poder crear un reclamo. (*)
- Accede a la aplicación en tu navegador: `http://127.0.0.1:8000/reclamo-listar/` para poder listar los reclamos. (*)

(*) Ambas opciones disponibles en el menu principal de la pagina.

## Tecnologías utilizadas

- Django
- Python
- SQL Lite DB
- Bootstrap (https://getbootstrap.com/)

