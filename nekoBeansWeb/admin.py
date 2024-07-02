from django.contrib import admin
from .models import Genero, Usuario, Producto, Contacto, Plantilla, TrabajaConNosotros, Carrito, ItemCarrito


# Register your models here.

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id_genero', 'genero')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nickname', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'id_genero', 'telefono', 'email', 'direccion', 'user_verificado')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'precio', 'tipo_modo_uso', 'colores', 'creador', 'categoria')

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email', 'telefono', 'tipo_solicitud')
    search_fields = ('nombre', 'apellidos', 'email', 'telefono')
    list_filter = ('tipo_solicitud',)

@admin.register(Plantilla)
class PlantillaAdmin(admin.ModelAdmin):
    list_display = ('nombrePlantilla', 'tipo_modo_uso', 'categoria')
    search_fields = ('nombrePlantilla', 'categoria')
    list_filter = ('tipo_modo_uso', 'categoria')

@admin.register(TrabajaConNosotros)
class TrabajaConNosotrosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'rut', 'region', 'fecha_nacimiento', 'nombre_usuario')
    search_fields = ('nombre', 'apellidos', 'rut', 'region')

    def nombre_usuario(self, obj):
        return obj.usuario.username

    nombre_usuario.short_description = 'Usuario'



@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'creado', 'subtotal')
    readonly_fields = ('creado', 'subtotal')

    def subtotal(self, obj):
        return obj.get_subtotal()

@admin.register(ItemCarrito)
class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ('carrito', 'nombre_producto', 'cantidad', 'total_precio')
    readonly_fields = ('carrito', 'producto', 'cantidad')

    def nombre_producto(self, obj):
        return obj.producto.titulo

    def total_precio(self, obj):
        return obj.get_total_precio()

    nombre_producto.short_description = 'Producto'  # Cambia el nombre de la columna en el admin
    total_precio.short_description = 'Total Precio'

