
from django.urls import path


# importamos las vistas de autores, libros y editoriales.
from .views import (
    editoriales_view,
    editorial_detail,
    autores_view, 
    autor_detail,
    libro_detail,
    libros_view,
)

#indicamos el nombre de la aplicación para poder usar el tercer parámetro del path
app_name="books"

urlpatterns = [
    path("editoriales/", editoriales_view, name="editorial_list"),  
    path("editoriales/<int:id>/", editorial_detail, name="editorial_detail"),  
   
    path("autores/", autores_view, name="autor_list"),  
    path("autores/<int:id>/", autor_detail, name="autor_detail"),  # Solo machea con autores/# siendo # un número.
    
    path("libros/", libros_view, name="libro_list"),   
    path("libros/<int:id>/", libro_detail, name="libro_detail"),
]

    




