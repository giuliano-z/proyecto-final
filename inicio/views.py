from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from inicio.models import Libro
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from inicio.forms import BusquedaFormulario
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from inicio.forms import CrearLibroFormulario, ModificarLibroFormulario
from django.utils import timezone


# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

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

class CrearLibro(LoginRequiredMixin, CreateView):
    model = Libro
    template_name = 'inicio/CBV/crear_libro_CBV.html'
    form_class = CrearLibroFormulario
    success_url = reverse_lazy('inicio:lista_libros')

    def form_valid(self, form):
        form.instance.propietario = self.request.user
        form.instance.fecha_creacion = timezone.now()
        form.instance.imagen = self.request.FILES.get('imagen')
        return super().form_valid(form)
        
class ModificarLibro(LoginRequiredMixin, UpdateView):
    model = Libro
    template_name = 'inicio/CBV/modificar_libro_CBV.html'
    form_class = ModificarLibroFormulario
    success_url = reverse_lazy('inicio:lista_libros')

    def form_valid(self, form):
        form.instance.imagen = self.request.FILES.get('imagen')
        return super().form_valid(form)

class EliminarLibro(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name ="inicio/CBV/eliminar_libro_CBV.html"
    success_url = reverse_lazy('inicio:lista_libros')

class  MostrarLibro(DetailView):
    model = Libro
    template_name = "inicio/CBV/mostrar_libro_CBV.html"

def sobre_nosotros(request):
    return render(request, 'inicio/sobre_nosotros.html')