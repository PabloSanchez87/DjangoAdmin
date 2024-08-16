## VISTAS GENERALES DE LA APLICACIÓN
""" 
Creamos las vistas generales de la aplicación:
    - home
    - contact
    
Las agrupación de vistas serán: autores, libros y editoriales.
"""

# Exploramos uso de URLS.
# Importamos render
from django.shortcuts import render, redirect
from books.models import Autor, Libro, Editorial
from books.forms import SearchForm
from .form import ContactForm
from django.contrib import messages

# Función modo ejemplo para enlazar con la un "home_view"
def home_view(request):
    return render(request, 'general/home.html')  # Render: Necesita un request y un template.
                                            # Busca el template en el archivo settings.py

                                            
# def contact_view(request):
#     if request.POST:
#         # Procesar los datos del formulario
#         nombre = request.POST['name']
#         email =request.POST['email']
#         mensaje =request.POST['message']
#         # Guardar los datos en la base de datos
#         print(f'El usaurio {nombre} con dirección {email} ha enviado el siguiente mensaje: {mensaje}')
    
#     return render(request, 'general/contact.html')



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario
            nombre = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['message']
            
            # Aquí podrías guardar los datos en la base de datos o enviar un correo
            print(f'El usuario {nombre} con dirección {email} ha enviado el siguiente mensaje: {mensaje}')
            
            context = {
                'form': form,
                'success': True
            }
            
            return render(request, 'general/contact.html', context)
        
    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'general/contact.html', context)






# def search_view(request):
#    #print(request.GET['query'])  # Imprime los parámetros GET de la petición HTTP
#     if request.GET:
#         busqueda = request.GET['query']  # Obtenemos el parámetro GET de la petición HTTP
#         autores = Autor.objects.filter(nombre__icontains=busqueda)
#         libros = Libro.objects.filter(titulo__icontains=busqueda)
#         editoriales = Editorial.objects.filter(nombre__icontains=busqueda)
        
#         context = {
#             'autores': autores,
#             'libros': libros,
#             'editoriales': editoriales,
#             }    
#         return render(request, 'general/search.html', context)
#     return render(request, 'general/search.html')



def search_view(request):
    form = SearchForm(request.GET or None)  # Inicializa el formulario con GET data si está presente

    # Inicializa las listas vacías para los resultados
    autores = []
    libros = []
    editoriales = []

    if form.is_valid():  # Verifica si el formulario es válido
        busqueda = form.cleaned_data.get('query')  # Obtén el valor de la búsqueda del formulario
        
        # Realiza la búsqueda en los modelos
        autores = Autor.objects.filter(nombre__icontains=busqueda)
        libros = Libro.objects.filter(titulo__icontains=busqueda)
        editoriales = Editorial.objects.filter(nombre__icontains=busqueda)

    # Actualiza el contexto con el formulario y los resultados (vacíos o con datos)
    context = {
        'form': form,
        'autores': autores,
        'libros': libros,
        'editoriales': editoriales,
    }

    return render(request, 'general/search.html', context)
