# Generated by Django 4.2.13 on 2024-07-16 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nekoBeansWeb', '0013_envio_fecha_pedido_alter_envio_apellido_materno_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='envio',
            name='fecha_pedido',
        ),
    ]