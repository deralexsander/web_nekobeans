from django.urls import path
from .views import (
    inicio, carrito, comentarios, como_funciona, crear, inicio_sesion, 
    problemas_pedido, productos, registrar_usuario, servicio_pedido, 
    trabaja_con_nosotros, crear_producto, listar_productos, modificar_producto, eliminar_producto
)

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('carrito/', carrito, name="carrito"),
    path('comentarios/', comentarios, name="comentarios"),
    path('como_funciona/', como_funciona, name="como_funciona"),
    path('crear/', crear, name="crear"),
    path('inicio-sesion/', inicio_sesion, name="inicio_sesion"),
    path('problemas-pedido/', problemas_pedido, name="problemas_pedido"),
    path('productos/', productos, name="productos"),
    path('registrar-usuario/', registrar_usuario, name="registrar_usuario"),
    path('servicio-pedido/', servicio_pedido, name="servicio_pedido"),
    path('trabaja-con-nosotros/', trabaja_con_nosotros, name="trabaja_con_nosotros"),
    path('crear-producto/', crear_producto, name='crear_producto'),
    path('listar-productos/', listar_productos, name='listar_productos'),
    path('modificar-producto/<id>/', modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/', eliminar_producto, name='eliminar_producto'),
]
