from django.shortcuts import render
from books.models import Libro
# Create your views here.
def libros_view(request):
    # libros = [
    #   {
    #       "id": 1,
    #       "nombre": "Don Quijote de la Mancha"
    #   },
    #   {
    #       "id": 2,
    #       "nombre": "Harry Potter y la piedra Filosofal"
    #   },
    #   {
    #       "id": 3,
    #       "nombre": "Clean Code"
    #   },
    # ]
    
    libros = Libro.objects.all()
    
    context = {
        "libros": libros,
        "titulo": "Libros. Usando contexto."
    }
    return render(request, 'libros/libros_list.html', context)

# Como está esperando un id para mostrar la lista que corresponde, tiene que pasarse como parámetro.
def libro_detail(request, id):
    libros = [
      {
          "id": 1,
          "nombre": "Don Quijote de la Mancha"
      },
      {
          "id": 2,
          "nombre": "Harry Potter y la piedra Filosofal"
      },
      {
          "id": 3,
          "nombre": "Clean Code"
      },
    ]

    context = {
        "libro": None,
    }
    for libro in libros:
        if libro['id'] == id:
            context['libro'] = libro
            break

    return render(request, 'libros/libro_detail.html', context)
