NekoBeans
=========

Proyecto web desarrollado con Django.

Para ejecutar en macOS o Linux:
1. Instala Python 3.10, 3.11 o 3.12.
2. En la carpeta del proyecto, crea y activa un entorno virtual:
   python3 -m venv .venv
   source .venv/bin/activate
3. Instala las dependencias:
   pip install -r requirements.txt
4. Inicia el servidor:
   python manage.py runserver
5. Abre http://127.0.0.1:8000/inicio/ en el navegador.

La base de datos local usa SQLite (db.sqlite3). No uses el servidor de
desarrollo de Django para publicar el sitio en producción.
