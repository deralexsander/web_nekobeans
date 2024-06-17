from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import floatformat
from .models import Producto
from .forms import ContactoForm, PlantillaForm, TrabajaConNosotrosForm, ProductoForm
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'nekoBeansWeb/inicio.html')
    
def crear(request):
    data = {
        'form': PlantillaForm()  # Utiliza PlantillaForm aquí
    }

    if request.method == 'POST':
        formulario = PlantillaForm(data=request.POST, files=request.FILES)  # Incluye files=request.FILES para la carga de imágenes
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Tu creación ha sido guardada con éxito"  # Corrige el mensaje de éxito
        else:
            data["form"] = formulario

    return render(request, 'nekoBeansWeb/crear.html', data)



def carrito(request):
    return render(request, 'nekoBeansWeb/carrito.html')

def comentarios(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Tu mensaje ha sido guardado con éxito"
        else:
            data["form"] = formulario

    return render(request, 'nekoBeansWeb/comentarios.html', data)

def como_funciona(request):
    return render(request, 'nekoBeansWeb/como_funciona.html')

def inicio_sesion(request):
    return render(request, 'nekoBeansWeb/registration/iniciar_sesion.html')

def problemas_pedido(request):
    return render(request, 'nekoBeansWeb/problemas_pedido.html')


def productos(request):
    productos = Producto.objects.all()

    for producto in productos:
        producto.precio_formateado = floatformat(producto.precio, -2)  # Formatea el precio con dos decimales y separadores de miles si es necesario

    data = {
        'productos': productos
    }
    return render(request, 'nekoBeansWeb/productos.html', data)

def registrar_usuario(request):
    return render(request, 'nekoBeansWeb/registration/registrar_usuario.html')

def servicio_pedido(request):
    return render(request, 'nekoBeansWeb/servicio_pedido.html')

def trabaja_con_nosotros(request):
    data = {
        'form': TrabajaConNosotrosForm()
    }

    if request.method == 'POST':
        formulario = TrabajaConNosotrosForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Tu mensaje ha sido guardado con éxito"
        else:
            data["form"] = formulario

    return render(request, 'nekoBeansWeb/trabaja_con_nosotros.html', data)

def crear_producto(request):
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Tu mensaje ha sido guardado con éxito"
        else:
            data["form"] = formulario


    return render(request, 'nekoBeansWeb/producto/agregar.html', data)

def listar_productos(request):
    productos = Producto.objects.all() 
    data = {
        'productos': productos
    }
    return render(request, 'nekoBeansWeb/producto/listar.html', data)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_productos')
    else:
        formulario = ProductoForm(instance=producto)

    data = {
        'form': formulario,
        'producto': producto
    }

    return render(request, 'nekoBeansWeb/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('listar_productos')