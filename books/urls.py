
from django.urls import path


# importamos las vistas de autores, libros y editoriales.
from .views import (
    editoriales_view,
    autores_view, 
    autor_detail,
    libros_view,
)

#indicamos el nombre de la aplicación para poder usar el tercer parámetro del path
app_name="books"

urlpatterns = [
    path("editoriales/", editoriales_view, name="editorial_list"),  
    path("autores/", autores_view, name="autor_list"),  
    
    # Solo machea con autores/# siendo # un número.
    path("autores/<int:id>/", autor_detail, name="autor_detail"),  
    
    path("libros/", libros_view, name="libro_list"),   
]

    




