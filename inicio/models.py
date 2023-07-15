from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    descripcion = models.TextField(null=True)
    imagen = models.ImageField(upload_to='fotos/', null=True, blank=True)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Libro: {self.titulo} - Autor: {self.autor} - Precio {self.precio} - Editorial: {self.editorial} - Propietario: {self.propietario.username}"
    