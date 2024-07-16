# Generated by Django 4.2.13 on 2024-07-16 17:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nekoBeansWeb', '0012_remove_envio_carrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='envio',
            name='fecha_pedido',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='envio',
            name='apellido_materno',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='envio',
            name='apellido_paterno',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='envio',
            name='direccion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='envio',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='envio',
            name='nickname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='envio',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='envio',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
    ]