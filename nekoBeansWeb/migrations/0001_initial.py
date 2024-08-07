# Generated by Django 4.2.13 on 2024-07-16 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=9)),
                ('tipo_solicitud', models.IntegerField(choices=[(1, 'Consulta'), (2, 'Reclamo'), (3, 'Sugerencia'), (4, 'Felicitaciones'), (5, 'Pedidos especiales')])),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('tipo_modo_uso', models.IntegerField(choices=[(1, 'Broche'), (2, 'Colgante')], default=1)),
                ('colores', models.CharField(max_length=200)),
                ('creador', models.CharField(max_length=20)),
                ('categoria', models.CharField(max_length=20)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=15)),
                ('contrasena_user', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=20)),
                ('apellido_materno', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=45)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('id_genero', models.ForeignKey(db_column='idGenero', on_delete=django.db.models.deletion.CASCADE, to='nekoBeansWeb.genero')),
            ],
        ),
        migrations.CreateModel(
            name='TrabajaConNosotros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=9, verbose_name='RUT')),
                ('region', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('carnet', models.ImageField(upload_to='identi_carnet')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plantilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePlantilla', models.CharField(max_length=20)),
                ('imagen', models.ImageField(null=True, upload_to='plantillas')),
                ('descripcion', models.CharField(max_length=100)),
                ('tipo_modo_uso', models.IntegerField(choices=[(1, 'Broche'), (2, 'Colgante')], default=1)),
                ('categoria', models.CharField(max_length=50)),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='nekoBeansWeb.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nekoBeansWeb.producto')),
            ],
        ),
        migrations.CreateModel(
            name='envio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.TextField()),
                ('productos', models.TextField(default='No hay productos')),
                ('estado_pedido', models.IntegerField(choices=[(1, 'En espera'), (2, 'En construccion'), (3, 'Listo!')], default=1)),
                ('forma_pago', models.IntegerField(choices=[(1, 'Efectivo'), (2, 'trasferencia'), (3, 'tarjeta')], default=1)),
                ('estado_pago', models.IntegerField(choices=[(1, 'Por pagar'), (2, 'Pagado')], default=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
