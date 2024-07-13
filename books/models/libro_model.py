from django.db import models
from .autor_model import Autor
from .editorial_model import Editorial

# Modelo para Libros
class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    isbn = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField()
    numero_paginas = models.IntegerField()
    
    #idioma = models.CharField(max_length=100)
    #Creamos un CHOICES de los idiomas posibles.
    LANGS_CHOICES = {
        "ES": "Español",
        "EN": "Inglés"
    }
    idioma = models.CharField(
        max_length=2, 
        choices=LANGS_CHOICES,
        default="ES"
    )
    
    #portada = models.ImageField(upload_to="portadas_libros/", null=True, blank=True)
    descripcion = models.TextField()
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)
    genero = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo