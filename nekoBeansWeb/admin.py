from django.contrib import admin
from .models import Genero, Cliente, Usuario, Colaborador, ModoUso, Producto

# Register your models here.

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id_genero', 'genero')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'id_genero', 'telefono', 'email', 'direccion')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nickname', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'id_genero', 'telefono', 'email', 'direccion', 'user_verificado')

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nickname', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'image_cedula', 'id_genero', 'telefono', 'email', 'direccion')

@admin.register(ModoUso)
class ModoUsoAdmin(admin.ModelAdmin):
    list_display = ('id_ModoUso', 'ModoUso')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'precio', 'id_ModoUso', 'colores', 'creador', 'categoria')
