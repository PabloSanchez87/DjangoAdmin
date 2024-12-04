from django import forms
from django.forms import ModelForm
from books.models import Libro

# Create your forms here.

class LibroModelFormCreate(ModelForm):
    class Meta:
        model = Libro
        fields = [
            'titulo',
            'isbn',
            'fecha_publicacion',
            'numero_paginas',
            'idioma',
            'descripcion',
            'editorial',
            'autores',
            'genero',
            'precio',
        ]
        
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
            'idioma': forms.Select(attrs={'class': 'form-control'}),
            'editorial': forms.Select(attrs={'class': 'form-control'}),
            'autores': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        
        
    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if len(titulo) < 5:
            raise forms.ValidationError("El titulo debe tener menos de 5 caracteres.")
        return titulo
    
            

    
        