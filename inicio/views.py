from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from inicio.models import Libro
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from inicio.forms import BusquedaFormulario
from django.views.generic.detail import DetailView

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

class CrearLibro(CreateView):
    model = Libro
    template_name = 'inicio/CBV/crear_libro_CBV.html'
    fields = ['titulo', 'autor', 'editorial','precio', 'descripcion']
    success_url = reverse_lazy('inicio:lista_libros')

class ListaLibro(ListView):
    model = Libro
    template_name = 'inicio/CBV/lista_libros_CBV.html'
    context_object_name = 'libros'

    def get_queryset(self):
        lista_libros = []
        formulario = BusquedaFormulario(self.request.GET)
        if formulario.is_valid():
            busqueda = formulario.cleaned_data['titulo']
            lista_libros = Libro.objects.filter(titulo__icontains=busqueda)
        return lista_libros

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['formulario'] = BusquedaFormulario()
        return contexto

class ModificarLibro(UpdateView):
    model = Libro 
    template_name = 'inicio/CBV/modificar_libro_CBV.html'
    fields = ['titulo', 'autor', 'editorial','precio', 'descripcion']
    success_url = reverse_lazy('inicio:lista_libros')

class EliminarLibro(DeleteView):
    model = Libro
    template_name ="inicio/CBV/eliminar_libro_CBV.html"
    success_url = reverse_lazy('inicio:lista_libros')

class  MostrarLibro(DetailView):
    model = Libro
    template_name = "inicio/CBV/mostrar_libro_CBV.html"
