from django.contrib import admin
from .models import Genero, Usuario, ModoUso, Producto
# Register your models here.
admin.site.register(Genero)
admin.site.register(Usuario)
admin.site.register(ModoUso)
admin.site.register(Producto)