# Generated by Django 4.2.13 on 2024-06-23 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nekoBeansWeb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='usuario',
        ),
    ]
