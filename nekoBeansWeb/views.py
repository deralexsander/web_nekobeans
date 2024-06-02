from django.shortcuts import render

def inicio(request):
    return render(request, 'nekoBeansWeb/inicio.html')
    
def crear(request):
    return render(request, 'nekoBeansWeb/crear.html')

def carrito(request):
    return render(request, 'nekoBeansWeb/carrito.html')

def comentarios(request):
    return render(request, 'nekoBeansWeb/comentarios.html')

def como_funciona(request):
    return render(request, 'nekoBeansWeb/como_funciona.html')

def inicio_sesion(request):
    return render(request, 'nekoBeansWeb/iniciar_sesion.html')

def problemas_pedido(request):
    return render(request, 'nekoBeansWeb/problemas_pedido.html')

def productos(request):
    return render(request, 'nekoBeansWeb/productos.html')

def registrar_usuario(request):
    return render(request, 'nekoBeansWeb/registrar_usuario.html')

def servicio_pedido(request):
    return render(request, 'nekoBeansWeb/servicio_pedido.html')

def trabaja_con_nosotros(request):
    return render(request, 'nekoBeansWeb/trabaja_con_nosotros.html')
