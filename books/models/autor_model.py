from django.db import models

# Modelo para Autores
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=100)
    biografia = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=20,null=True, blank=True)
    sitio_web = models.URLField(null=True, blank=True)
    premios = models.TextField(null=True, blank=True)
    #foto = models.ImageField(upload_to="autores_fotos/", null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"