from django.db import models

class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.genero
    
#USUARIOS
class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
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
    
class Colaborador(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nickname = models.CharField(max_length=15)
    contrasena_user = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    image_cedula = models.ImageField(upload_to='cedulas/') # Cambiado a ImageField
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE, db_column='idGenero')
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"

class ModoUso(models.Model):
    id_ModoUso = models.AutoField(db_column='idModoUso', primary_key=True)
    ModoUso = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.ModoUso

class Producto(models.Model):
    titulo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_ModoUso = models.ForeignKey(ModoUso, on_delete=models.CASCADE, db_column='idModoUso')
    colores = models.CharField(max_length=200)  # Aumenta la longitud del campo para acomodar múltiples colores
    creador = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.titulo

    def obtener_colores(self):
        return self.colores.split(',')  # Devuelve una lista de colores separados por comas
