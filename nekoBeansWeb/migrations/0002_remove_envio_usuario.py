# Generated by Django 4.2.13 on 2024-07-16 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nekoBeansWeb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='envio',
            name='usuario',
        ),
    ]