from django import forms
from .models import contacto, Plantilla, TrabajaConNosotros, Producto



class ContactoForm(forms.ModelForm): 
    class Meta:
        model = contacto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@gmail.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '911111111', 'onkeypress': 'return soloNumeros(event)'}),
            'tipo_solicitud': forms.Select(attrs={'class': 'form-select'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }



class PlantillaForm(forms.ModelForm):
    class Meta:
        model = Plantilla
        fields = '__all__'
        widgets = {
            'nombrePlantilla': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre '}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción'}),
            'id_ModoUso': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
        }

class TrabajaConNosotrosForm(forms.ModelForm):
    class Meta:
        model = TrabajaConNosotros
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'id': 'nombre'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'id': 'apellidos'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'id': 'rut', 'placeholder': 'Ej: 11111111-1'}),
            'region': forms.Select(attrs={'class': 'form-select', 'id': 'categoriasSelect'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'fecha'}),
            'carnet': forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'carnet'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'id_ModoUso': forms.Select(attrs={'class': 'form-select'}),
            'colores': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Colores separados por comas'}),
            'creador': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Creador'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }