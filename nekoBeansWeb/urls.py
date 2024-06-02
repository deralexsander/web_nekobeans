from django.urls import path
from .views import inicio, carrito, comentarios, como_funciona, crear, inicio_sesion, problemas_pedido, productos, registrar_usuario, servicio_pedido, trabaja_con_nosotros

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('carrito/', carrito, name="carrito"),
    path('comentarios/', comentarios, name="comentarios"),
    path('como_funciona/', como_funciona, name="como_funciona"),
    path('crear/', crear, name="crear"),
    path('inicio_sesion/', inicio_sesion, name="inicio_sesion"),
    path('problemas_pedido/', problemas_pedido, name="problemas_pedido"),
    path('productos/', productos, name="productos"),
    path('registrar_usuario/', registrar_usuario, name="registrar_usuario"),
    path('servicio_pedido/', servicio_pedido, name="servicio_pedido"),
    path('trabaja_con_nosotros/', trabaja_con_nosotros, name="trabaja_con_nosotros"),
]
