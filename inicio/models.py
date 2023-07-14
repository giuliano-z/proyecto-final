from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    descripcion = models.TextField(null=True)

    def __str__(self):
        return f"Libro: {self.titulo} - Autor: {self.autor} - Editorial: {self.editorial}"
