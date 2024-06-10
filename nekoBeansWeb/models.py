from django.db import models

class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.genero

class Usuario(models.Model):
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

class ModoUso(models.Model):
    id_ModoUso = models.AutoField(db_column='idModoUso', primary_key=True)
    ModoUso = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.ModoUso

class Producto(models.Model):
    titulo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    precio = models.CharField(primary_key=True, max_length=10)
    id_ModoUso = models.ForeignKey(ModoUso, on_delete=models.CASCADE, db_column='idModoUso')
    colores = models.CharField(max_length=20)
    creador = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)

    def __str__(self):
        return self.Producto