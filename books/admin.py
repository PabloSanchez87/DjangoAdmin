from django.contrib import admin

from .models import Editorial, Autor, Libro

# Register your models here.

##inlines ( tiene sentido cuando algo esta relacionado con algo a través de una Foreing key)
## Opcion 1: TAbularInLine, los campos a cubrir se expanden horizontalmente
## Opcion 3: StakedInLine, los campos a cubrir se expanden verticalmente.
class BookInLine(admin.StackedInline):
    model = Libro
    

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    ## List_display nos permite configurar los parámetros que queremos mostrar.
   list_display = ["pk",
                   "nombre",  
                   "ciudad", 
                   "telefono", 
                   "sitio_web",
                   "fecha_fundacion"]
   
   ## Nos sirve para filtrar por el parámetro.
   list_filter = ["fecha_fundacion"]

##Inline   
   inlines = [
       BookInLine,
   ]
   

    
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ["pk",
                    "nombre",
                    "apellido",
                    "fecha_nacimiento", 
                    "email", 
                    "telefono"]
    
    ## Que orden por defecto quiero que tenga el listado. (- para ordenar a la inversa)
    ordering = ["-nombre", "apellido"]
    

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ["titulo", 
                    "editorial",
                    "isbn", 
                    "fecha_publicacion", 
                    "numero_paginas", 
                    "idioma", 
                    ]
    ## Nos sirve para filtrar por el parámetro.
    list_filter = ["editorial", "idioma"]
    
    ## Nos permite buscar por un campo del propio libro, o incluso por un campo relacionado como es el nombre de un autor.
    search_fields = ["titulo", "autores__nombre"]
    
    ##el filter_horizontal nos cambiar el desplegable de los autores a elegir que tenía un multiselect.
    filter_horizontal = ["autores"]
    
   
