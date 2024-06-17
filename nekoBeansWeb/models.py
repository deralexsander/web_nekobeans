from django.db import models

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
    user_verificado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"
    
tipo_uso = [
        (1, 'broche'),
        (2, 'colgante'),
        (3, 'ambos'),

]

class Producto(models.Model):
    titulo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_modo_uso = models.IntegerField(choices=tipo_uso, default=1)
    colores = models.CharField(max_length=200)  # Aumenta la longitud del campo para acomodar múltiples colores
    creador = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.titulo

    def obtener_colores(self):
        return self.colores.split(',')  # Devuelve una lista de colores separados por comas

tipo_consulta = [
        (1, 'Consulta'),
        (2, 'Reclamo'),
        (3, 'Sugerencia'),
        (4, 'Felicitaciones'),
        (5, 'Pedidos especiales'),
]


class contacto(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    email = models.EmailField()
    telefono = models.CharField(max_length=9)
    tipo_solicitud = models.IntegerField(choices=tipo_consulta)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
    


class Plantilla(models.Model):
    nombrePlantilla = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to="productos", null=True)
    descripcion = models.CharField(max_length=100)
    tipo_modo_uso = models.IntegerField(choices=tipo_uso, default=1)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombrePlantilla


class TrabajaConNosotros(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    region = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    carnet = models.ImageField(upload_to='carnets')

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'
