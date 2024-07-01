from django.urls import path
from .views import (
    inicio, comentarios, como_funciona, crear, login, 
    problemas_pedido, productos, registro, servicio_pedido, 
    trabaja_con_nosotros, crear_producto, listar_productos, 
    modificar_producto, eliminar_producto, perfil, listar_plantilla,
    eliminar_plantilla, lista_comentarios, eliminar_contacto, listar_peticiones, eliminar_peticiones
)

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('comentarios/', comentarios, name="comentarios"),
    path('lista-comentarios/', lista_comentarios, name="lista_comentarios"),
    path('como_funciona/', como_funciona, name="como_funciona"),
    path('crear/', crear, name="crear"),
    path('listar-plantilla/', listar_plantilla, name='listar_plantilla'),
    path('login/', login, name="login"),
    path('perfil/', perfil, name="perfil"),
    path('problemas-pedido/', problemas_pedido, name="problemas_pedido"),
    path('productos/', productos, name="productos"),
    path('registro/', registro, name="registro"),
    path('servicio-pedido/', servicio_pedido, name="servicio_pedido"),
    path('trabaja-con-nosotros/', trabaja_con_nosotros, name="trabaja_con_nosotros"),
    path('crear-producto/', crear_producto, name='crear_producto'),
    path('crear-producto/<int:plantilla_id>/', crear_producto, name='crear_producto_con_plantilla'),
    path('listar-productos/', listar_productos, name='listar_productos'),
    path('modificar-producto/<int:id>/', modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<int:id>/', eliminar_producto, name='eliminar_producto'),
    path('eliminar-plantilla/<int:id>/', eliminar_plantilla, name='eliminar_plantilla'),
    path('eliminar-contacto/<int:id>/', eliminar_contacto, name='eliminar_contacto'),
    path('lista-peticiones/', listar_peticiones, name='lista_peticiones'),
    path('eliminar-peticiones/<int:id>/', eliminar_peticiones, name='eliminar_peticiones'),

]
