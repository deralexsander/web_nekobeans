# Generated by Django 4.2.13 on 2024-07-01 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nekoBeansWeb', '0004_alter_plantilla_tipo_modo_uso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajaconnosotros',
            name='rut',
            field=models.CharField(max_length=9, verbose_name='RUT'),
        ),
    ]