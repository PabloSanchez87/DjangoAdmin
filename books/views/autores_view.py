from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

from books.models import Autor
from books.forms import AutorModelFormCreate


# Create your views here.
def autores_view(request): 
    '''
    ## Muestra de como pasarle datos a nuestra vista.
    # Podemos verlo con debug_tools en la pestaña plantilla.
    # autores = [
    #   {
    #       "id": 1,
    #       "nombre": "Antonio", 
    #       "f_nac": date(1980,8,1)
    #   },
    #   {
    #       "id": 2,
    #       "nombre": "Felipe",
    #       "f_nac": date(1985,8,11)
    #   },
    #   {
    #       "id": 3,
    #       "nombre": "Matilde",
    #       "f_nac": date(1990,9,30)
    #   },
    # ]
    '''    
    autores = Autor.objects.all()  # Obtén todos los objetos del modelo Autor
    
    context = {
        "autores": autores,
        }
    
    
    return render(request, 'autores/autores_list.html', context)


# Como está esperando un id para mostrar la lista que corresponde, tiene que pasarse como parámetro.
def autor_detail(request, id):
    '''
    autores = [
      {
          "id": 1,
          "nombre": "Antonio", 
          "f_nac": date(1980,8,1)
      },
      {
          "id": 2,
          "nombre": "Felipe",
          "f_nac": date(1985,8,11)
      },
      {
          "id": 3,
          "nombre": "Matilde",
          "f_nac": date(1990,9,30)
      },
    ]
    '''
    autor = get_object_or_404(Autor, pk=id)

    context = {
        "autor": autor,
    }
            
    return render(request, 'autores/autor_detail.html', context)


def autor_create(request):
    if request.POST:
        form = AutorModelFormCreate(request.POST)
        if form.is_valid():
            nuevo_autor = form.save()
            
            # Redireccionamos a al vista detalle de la autor creada
            return redirect(reverse('books:autor_detail', kwargs={'id': nuevo_autor.pk}))
    else: 
        form = AutorModelFormCreate()
        
    context = {
        "form": form,
    }
        
    return render(request, 'autores/autor_create.html',context=context)