from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.genero
    
    
class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nickname = models.CharField(max_length=15)
    contrasena_user = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE, db_column='idGenero')
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"

    
tipo_uso = [
    (1, 'Broche'),
    (2, 'Colgante'),
]

class Plantilla(models.Model):
    nombrePlantilla = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to="plantillas", null=True)
    descripcion = models.CharField(max_length=100)
    tipo_modo_uso = models.IntegerField(choices=tipo_uso, default=1)
    categoria = models.CharField(max_length=50)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):
        return self.nombrePlantilla

class Producto(models.Model):
    titulo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    tipo_modo_uso = models.IntegerField(choices=tipo_uso, default=1)
    colores = models.CharField(max_length=200)
    creador = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.titulo

    def obtener_colores(self):
        return self.colores.split(',')

    @property
    def nombre_modo_uso(self):
        return dict(tipo_uso).get(self.tipo_modo_uso, "Desconocido")



tipo_consulta = [
        (1, 'Consulta'),
        (2, 'Reclamo'),
        (3, 'Sugerencia'),
        (4, 'Felicitaciones'),
        (5, 'Pedidos especiales'),
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    email = models.EmailField()
    telefono = models.CharField(max_length=9)
    tipo_solicitud = models.IntegerField(choices=tipo_consulta)
    mensaje = models.TextField()

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'
    


class TrabajaConNosotros(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=9, verbose_name='RUT')
    region = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    carnet = models.ImageField(upload_to='identi_carnet')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'




class Carrito(models.Model):
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Carrito {self.id}'

    def get_subtotal(self):
        return sum(item.get_total_precio() for item in self.items.all())

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.titulo}' 

    def get_total_precio(self):
        return self.cantidad * self.producto.precio

forma_pago = [
    (1, 'Efectivo'),
    (2, 'trasferencia'),
    (3, 'tarjeta'),
]

estado_pago = [
    (1, 'Por pagar'),
    (2, 'Pagado'),
]

estado_pedido = [
    (1, 'En espera'),
    (2, 'En construccion'),
    (3, 'Listo!'),
]

entrega = [
    (1, 'Pendiente'),
    (2, 'Entregado!'),
]

class envio(models.Model):
    nickname = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.TextField()
    productos = models.TextField(default='No hay productos')  # Valor por defecto
    estado_pedido = models.IntegerField(choices=estado_pedido, default=1)
    forma_pago = models.IntegerField(choices=forma_pago, default=1)
    estado_pago = models.IntegerField(choices=estado_pago, default=1)
    entrega = models.IntegerField(choices=entrega, default=1)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"

@receiver(pre_save, sender=envio)
def actualizar_estado_pago(sender, instance, **kwargs):
    if instance.forma_pago in [2, 3]: 
        instance.estado_pago = 2  