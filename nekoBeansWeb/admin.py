from django.contrib import admin
from .models import Genero, Usuario, ModoUso, Producto, contacto, Plantilla, TrabajaConNosotros


# Register your models here.

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id_genero', 'genero')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nickname', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'id_genero', 'telefono', 'email', 'direccion', 'user_verificado')

@admin.register(ModoUso)
class ModoUsoAdmin(admin.ModelAdmin):
    list_display = ('id_ModoUso', 'ModoUso')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'precio', 'id_ModoUso', 'colores', 'creador', 'categoria')

@admin.register(contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email', 'telefono', 'tipo_solicitud')
    search_fields = ('nombre', 'apellidos', 'email', 'telefono')
    list_filter = ('tipo_solicitud',)


@admin.register(Plantilla)
class PlantillaAdmin(admin.ModelAdmin):
    list_display = ('nombrePlantilla', 'id_ModoUso', 'categoria')
    search_fields = ('nombrePlantilla', 'categoria')
    list_filter = ('id_ModoUso', 'categoria')

@admin.register(TrabajaConNosotros)
class TrabajaConNosotrosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'rut', 'region', 'fecha_nacimiento')
    search_fields = ('nombre', 'apellidos', 'rut', 'region')
