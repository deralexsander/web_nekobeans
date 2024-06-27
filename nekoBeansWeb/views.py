from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import floatformat
from .models import Producto, Plantilla, Contacto, TrabajaConNosotros
from .forms import ContactoForm, PlantillaForm, TrabajaConNosotrosForm, ProductoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


def inicio(request):
    return render(request, 'nekoBeansWeb/inicio.html')
    
@login_required
def crear(request):
    if request.method == 'POST':
        formulario = PlantillaForm(request.POST, request.FILES)
        if formulario.is_valid():
            plantilla = formulario.save(commit=False)
            plantilla.creador = request.user  
            plantilla.save()
            return redirect('crear')  
    else:
        formulario = PlantillaForm()

    data = {
        'form': formulario
    }

    return render(request, 'nekoBeansWeb/crearplantilla/crear.html', data)

@permission_required('nekoBeansWeb.view_plantilla')
def listar_plantilla(request):
    plantillas = Plantilla.objects.all() 
    data = {
        'plantillas': plantillas
    }
    return render(request, 'nekoBeansWeb/crearplantilla/listar_crear.html', data)

@login_required
def carrito(request):
    return render(request, 'nekoBeansWeb/carrito.html')

@login_required
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

    return render(request, 'nekoBeansWeb/comentarios/comentarios.html', data)


def como_funciona(request):
    return render(request, 'nekoBeansWeb/como_funciona.html')

@login_required
def perfil(request):
    return render(request, 'nekoBeansWeb/perfil.html')



from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  # Cambia 'home' por la URL a la que quieras redirigir después del inicio de sesión
        else:
            messages.warning(request, 'Usuario o contraseña incorrectos')
    return render(request, 'nekoBeansWeb/login.html')




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


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            django_login(request, user) 
            messages.success(request, "te has registrado con exito!")
            return redirect(to="inicio")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)


def servicio_pedido(request):
    return render(request, 'nekoBeansWeb/servicio_pedido.html')

@login_required
def trabaja_con_nosotros(request):
    data = {
        'form': TrabajaConNosotrosForm()
    }

    if request.method == 'POST':
        formulario = TrabajaConNosotrosForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            trabaja_con_nosotros_instance = formulario.save(commit=False)
            trabaja_con_nosotros_instance.usuario = request.user
            trabaja_con_nosotros_instance.save()
            return redirect('trabaja_con_nosotros')
        else:
            data['form'] = formulario

    return render(request, 'nekoBeansWeb/trabajaconnosotros/trabaja_con_nosotros.html', data)

@permission_required('nekoBeansWeb.add_producto')
def crear_producto(request, plantilla_id=None):
    plantilla = None
    initial_data = {}
    if plantilla_id:
        plantilla = get_object_or_404(Plantilla, id=plantilla_id)
        initial_data = {
            'titulo': plantilla.nombrePlantilla,
            'descripcion': plantilla.descripcion,
            'tipo_modo_uso': plantilla.tipo_modo_uso,
            'categoria': plantilla.categoria,
            'creador': plantilla.creador,
            'imagen': plantilla.imagen  # Asegúrate de que este campo está aquí
        }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            producto = formulario.save(commit=False)
            producto.creador = request.user
            producto.save()
            
            if plantilla:
                plantilla.delete()

            return redirect('listar_productos')
    else:
        formulario = ProductoForm(initial=initial_data)

    data = {
        'form': formulario
    }

    return render(request, 'nekoBeansWeb/producto/agregar.html', data)

@permission_required('nekoBeansWeb.view_producto')
def listar_productos(request):
    productos = Producto.objects.all() 
    data = {
        'productos': productos
    }
    return render(request, 'nekoBeansWeb/producto/listar.html', data)

@permission_required('nekoBeansWeb.change_producto')
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

@permission_required('nekoBeansWeb.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('listar_productos')

@permission_required('nekoBeansWeb.delete_plantilla')
def eliminar_plantilla(request, id):
    plantilla = get_object_or_404(Plantilla, id=id)
    plantilla.delete()
    return redirect('listar_plantilla')

@permission_required('nekoBeansWeb.view_comentarios')
def lista_comentarios(request):
    contactos = Contacto.objects.all() 
    data = {
        'contactos': contactos
    }
    return render(request, 'nekoBeansWeb/comentarios/lista_contacto.html', data)

@permission_required('nekoBeansWeb.delete_contacto')
def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    contacto.delete()
    return redirect('lista_comentarios')

@permission_required('nekoBeansWeb.view_trabajaconnosotros')
def listar_peticiones(request):
    peticiones = TrabajaConNosotros.objects.all() 
    data = {
        'peticiones': peticiones
    }
    return render(request, 'nekoBeansWeb/trabajaconnosotros/lista_peticiones.html', data)

@permission_required('nekoBeansWeb.delete_trabajaconnosotros')
def eliminar_peticiones(request, id):
    peticion = get_object_or_404(TrabajaConNosotros, id=id)
    peticion.delete()
    return redirect('lista_peticiones')

