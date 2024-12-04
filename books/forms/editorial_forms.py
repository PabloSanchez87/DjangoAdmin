from django import forms
from django.forms import ModelForm
from books.models import Editorial

# Create your forms here.
class EditorialCreate(forms.Form):
    nombre = forms.CharField(max_length=200)
    direccion = forms.CharField(max_length=300, required=False)
    ciudad = forms.CharField(max_length=100, required=False)
    estado = forms.CharField(max_length=100, required=False)
    pais = forms.CharField(max_length=100, required=False)
    codigo_postal = forms.CharField(max_length=20, required=False)
    telefono = forms.CharField(max_length=20, required=False)
    email = forms.EmailField()
    sitio_web = forms.URLField(required=False)
    fecha_fundacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 5:
            raise forms.ValidationError("El nombre debe tener menos de 5 caracteres.")
        return nombre
    

#ModelForm
class EditorialModelFormCreate(ModelForm):
    class Meta:
        model = Editorial
        fields = [
            'nombre', 
            'direccion', 
            'ciudad', 'estado', 
            'pais', 
            'codigo_postal', 
            'telefono', 
            'email', 
            'sitio_web', 
            'fecha_fundacion'
            ]
    