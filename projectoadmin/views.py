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

# Función modo ejemplo para enlazar con la un "home_view"
def home_view(request):
    return render(request, 'home.html')  # Render: Necesita un request y un template.
                                            # Busca el template en el archivo settings.py

                                            
def contact_view(request):
    return render(request, 'contact.html')