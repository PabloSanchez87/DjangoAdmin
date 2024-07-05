from django.contrib import admin

from .models import Editorial, Autor, Libro

# Register your models here.


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
   pass
    
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    pass

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    pass