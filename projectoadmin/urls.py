# Ayuda para saber como utilizar las URLS.
"""projectoadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#from django.conf.urls import include # grappelli include
from django.shortcuts import redirect 
from debug_toolbar.toolbar import debug_toolbar_urls

""" --> urlpatters inicial antes de explorar uso de urls.
urlpatterns = [
   # path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('admin/', permanent=True)),  # Redirigir la raíz a /admin
] + debug_toolbar_urls() ## Añadimos las urls de debug_toolbar
"""

# importamos las vistas.
from .views import home_view, contact_view

# importamos las vistas de autores, libros y editoriales.
from books.views import (
    editoriales_view, 
    libros_view, 
    autores_view
)

# urlpatterns modificado explorando uso urls.
urlpatterns = [
    path("", home_view),  # raíz del sitio. 
    path("home/", home_view),  
    
    # Esto sería una forma de hacerlo. Pero podemos modularizarlo.
    # path("editoriales/", editoriales_view),  
    # path("autores/", autores_view),  
    # path("libros/", libros_view),  
    
    
    path("contact/", contact_view),  
    path('admin/', admin.site.urls),
] + debug_toolbar_urls()

    




