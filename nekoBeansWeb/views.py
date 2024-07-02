from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import floatformat
from .models import Producto, Plantilla, Contacto, TrabajaConNosotros, Carrito, ItemCarrito
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
            messages.success(request, "¡Has publicado tu creación con éxito!")
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
def comentarios(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tu mensaje ha sido guardado con éxito")
        else:
            data["form"] = formulario

    return render(request, 'nekoBeansWeb/comentarios/comentarios.html', data)


def como_funciona(request):
    return render(request, 'nekoBeansWeb/como_funciona.html')

@login_required
def perfil(request):
    return render(request, 'nekoBeansWeb/perfil.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  # Redirige a la página de inicio después del inicio de sesión exitoso
        else:
            messages.warning(request, 'Usuario o contraseña incorrectos')  # Muestra un mensaje de advertencia
    return render(request, 'nekoBeansWeb/login.html')




def problemas_pedido(request):
    return render(request, 'nekoBeansWeb/problemas_pedido.html')


def productos(request):
    productos = Producto.objects.all()

    for producto in productos:
        producto.precio_formateado = floatformat(producto.precio) 

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
            messages.success(request, "¡Te has registrado con éxito!")
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
            messages.success(request, "¡Te has registrado con éxito en la postulación!")
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
            'imagen': plantilla.imagen
        }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            producto = formulario.save(commit=False)
            producto.creador = request.user
            producto.save()
            messages.success(request, "¡Producto creado con éxito!")
            
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
            messages.success(request, "¡Modificaste el producto con éxito!")
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

@login_required
def agregar_al_carrito(request, producto_id):
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        try:
            carrito = Carrito.objects.get(id=carrito_id)
        except Carrito.DoesNotExist:
            carrito = Carrito.objects.create()
            request.session['carrito_id'] = carrito.id
    else:
        carrito = Carrito.objects.create()
        request.session['carrito_id'] = carrito.id

    producto = get_object_or_404(Producto, id=producto_id)

    # Agregar el producto al carrito
    item_carrito, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        item_carrito.cantidad += 1
        item_carrito.save()
        messages.success(request, "¡Producto agregado al carrito!")

    return redirect('productos')




@login_required
def obtener_carrito(request):
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        try:
            return Carrito.objects.get(id=carrito_id)
        except Carrito.DoesNotExist:
            return None
    else:
        return None

@login_required
def vaciar_carrito(request):
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        try:
            carrito = Carrito.objects.get(id=carrito_id)
            carrito.items.all().delete()  # Eliminar todos los items del carrito
            carrito.delete()  # Eliminar el carrito
            messages.success(request, "¡Productos eliminados de tu carrito!")
            request.session['carrito_id'] = None
        except Carrito.DoesNotExist:
            pass

    return redirect('ver_carrito')



@login_required
def ver_carrito(request):
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        try:
            carrito = Carrito.objects.get(id=carrito_id)
            items = carrito.items.all()
        except Carrito.DoesNotExist:
            carrito = None
            items = []
    else:
        carrito = None
        items = []

    return render(request, 'nekoBeansWeb/ver_carrito.html', {'carrito': carrito, 'items': items})




@login_required
def eliminar_del_carrito(request, item_id):
    
    #eliminar producto del carrito
    item = get_object_or_404(ItemCarrito, id=item_id)
    carrito = item.carrito
    item.delete()

    #eliminar el carro en caso de no quedar productos
    if not carrito.items.exists():
        carrito.delete()
        messages.success(request, "¡Producto eliminado de tu carrito!")
        request.session['carrito_id'] = None

    return redirect('ver_carrito')