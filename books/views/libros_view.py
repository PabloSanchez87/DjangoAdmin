from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

from books.models import Libro
from books.forms import LibroModelFormCreate


# Create your views here.
def libros_view(request):

    libros = Libro.objects.all()
    
    context = {
        "libros": libros,
    }
    
    return render(request, 'libros/libros_list.html', context)

# Como está esperando un id para mostrar la lista que corresponde, tiene que pasarse como parámetro.
def libro_detail(request, id):

    libro = get_object_or_404(Libro, pk=id)

    context = {
        "libro": libro,
    }

    return render(request, 'libros/libro_detail.html', context)


def libro_create(request):
    if request.POST:
        form = LibroModelFormCreate(request.POST)
        if form.is_valid():
            nuevo_libro = form.save(commit=False) # No guardamos el libro
            nuevo_libro.save() # Guardamos el libro
            form.save_m2m() # Guardamos los autores ManyToMany
            # Redireccionamos a al vista detalle de la autor creada
            return redirect(reverse('books:libro_detail', kwargs={'id': nuevo_libro.pk}))
    else:
        form = LibroModelFormCreate()
        
    context = {
        "form": form,
    }
    
    return render(request, 'libros/libro_create.html', context)