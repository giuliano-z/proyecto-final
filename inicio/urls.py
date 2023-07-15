from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros', views.ListaLibro.as_view(), name='lista_libros'),
    path('libro/crear', views.CrearLibro.as_view(), name='crear_libro'),
    path('libro/eliminar/<int:pk>/', views.EliminarLibro.as_view(), name='eliminar_libro'),
    path('libro/modificar/<int:pk>/', views.ModificarLibro.as_view(), name='modificar_libro'),
    path('libro/<int:pk>/', views.MostrarLibro.as_view(), name='mostrar_libro'),
    path('sobre_nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
]