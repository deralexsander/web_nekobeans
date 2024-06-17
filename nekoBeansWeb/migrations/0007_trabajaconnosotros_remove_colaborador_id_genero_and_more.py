# Generated by Django 4.2.13 on 2024-06-16 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nekoBeansWeb', '0006_alter_contacto_telefono_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrabajaConNosotros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=12)),
                ('region', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('carnet', models.ImageField(upload_to='carnets')),
            ],
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='id_genero',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Colaborador',
        ),
    ]
