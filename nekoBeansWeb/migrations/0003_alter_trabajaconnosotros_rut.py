# Generated by Django 4.2.13 on 2024-06-28 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nekoBeansWeb', '0002_remove_contacto_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajaconnosotros',
            name='rut',
            field=models.CharField(max_length=12, verbose_name='RUT'),
        ),
    ]
