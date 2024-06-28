from django import forms
from .models import Contacto, Plantilla, TrabajaConNosotros, Producto
from django.contrib.auth.forms import UserCreationForm



class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@gmail.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9\-]*', 'placeholder': '911111111', 'onkeypress': 'return soloNumeros(event)'}),
            'tipo_solicitud': forms.Select(attrs={'class': 'form-select'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }



class PlantillaForm(forms.ModelForm):
    class Meta:
        model = Plantilla
        fields = ['nombrePlantilla', 'imagen', 'descripcion', 'tipo_modo_uso', 'categoria']
        widgets = {
            'nombrePlantilla': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de tu plantilla'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción/detalle de la plantilla'}),
            'tipo_modo_uso': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoria'}),
        }

class TrabajaConNosotrosForm(forms.ModelForm):
    class Meta:
        model = TrabajaConNosotros
        fields = ['nombre', 'apellidos', 'rut', 'region', 'fecha_nacimiento', 'carnet']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT', 'pattern': '[0-9\-]*', 'title': 'Debe contener solo números'}),
            'region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Región'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'carnet': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'tipo_modo_uso': forms.Select(attrs={'class': 'form-select'}),
            'colores': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Colores separados por comas'}),
            'creador': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Creador'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CustomUserCreationForm(UserCreationForm):
    pass