from django import forms

class LibroFormularioBase(forms.Form):
    titulo = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=50)
    editorial = forms.CharField(max_length=50)

class CrearLibroFormulario(LibroFormularioBase):
    ...
    
class ModificarLibroFormulario(LibroFormularioBase):
    ...
    
class BusquedaFormulario(forms.Form):
    titulo = forms.CharField(max_length=100, required=False)