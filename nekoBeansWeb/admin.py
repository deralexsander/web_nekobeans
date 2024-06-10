from django.contrib import admin
from .models import Genero, Cliente, Usuario, Colaborador, ModoUso, Producto
# Register your models here.
admin.site.register(Genero)
admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Colaborador)
admin.site.register(ModoUso)
admin.site.register(Producto)