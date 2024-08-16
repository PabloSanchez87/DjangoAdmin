## VISTAS GENERALES DE LA APLICACIÓN
""" 
Creamos las vistas generales de la aplicación:
    - home
    - contact
    
Las agrupación de vistas serán: autores, libros y editoriales.
"""


# Exploramos uso de URLS.
# Importamos render
from django.shortcuts import render
from books.models import Autor, Libro, Editorial


# Función modo ejemplo para enlazar con la un "home_view"
def home_view(request):
    return render(request, 'general/home.html')  # Render: Necesita un request y un template.
                                            # Busca el template en el archivo settings.py

                                            
def contact_view(request):
    if request.POST:
        # Procesar los datos del formulario
        nombre = request.POST['name']
        email =request.POST['email']
        mensaje =request.POST['message']
        # Guardar los datos en la base de datos
        print(f'El usaurio {nombre} con dirección {email} ha enviado el siguiente mensaje: {mensaje}')
    
    return render(request, 'general/contact.html')


def search_view(request):
    
    
   #print(request.GET['query'])  # Imprime los parámetros GET de la petición HTTP
    if request.GET:
        busqueda = request.GET['query']  # Obtenemos el parámetro GET de la petición HTTP
        autores = Autor.objects.filter(nombre__icontains=busqueda)
        libros = Libro.objects.filter(titulo__icontains=busqueda)
        editoriales = Editorial.objects.filter(nombre__icontains=busqueda)
        
        context = {
            'autores': autores,
            'libros': libros,
            'editoriales': editoriales,
            }    
        return render(request, 'general/search.html', context)
    return render(request, 'general/search.html')