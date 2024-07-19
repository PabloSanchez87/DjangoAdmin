
from django.urls import path


# importamos las vistas de autores, libros y editoriales.
from .views import (
    editoriales_view,
    autores_view, 
    libros_view
)

urlpatterns = [
    
    path("editoriales/", editoriales_view),  
    path("autores/", autores_view),  
    path("libros/", libros_view),  
    
]

    




