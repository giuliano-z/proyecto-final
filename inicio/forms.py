from django import forms
from .models import Libro

class LibroFormularioBase(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'editorial', 'precio', 'descripcion', 'imagen']

class CrearLibroFormulario(LibroFormularioBase):
    ...

class ModificarLibroFormulario(LibroFormularioBase):
    ...

class BusquedaFormulario(forms.Form):
    titulo = forms.CharField(max_length=100, required=False)