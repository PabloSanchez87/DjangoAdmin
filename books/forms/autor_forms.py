from django import forms
from django.forms import ModelForm
from books.models import Autor

# Create your forms here.

    

#ModelForm
class AutorModelFormCreate(ModelForm):
    class Meta:
        model = Autor
        fields = [
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'nacionalidad',
            'biografia',
            'email',
            'telefono',
            'sitio_web',
            'premios',
        ]
        
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 5:
            raise forms.ValidationError("El nombre debe tener menos de 5 caracteres.")
        return nombre
            

    
        