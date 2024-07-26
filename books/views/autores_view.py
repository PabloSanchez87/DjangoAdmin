from django.shortcuts import render
from datetime import date

# Create your views here.
def autores_view(request):     
    ## Muestra de como pasarle datos a nuestra vista.
    # Podemos verlo con debug_tools en la pestaña plantilla.
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
    
    context = {
        "autores": autores,
        "titulo": "Autores. Usando contexto."
    }
    
    
    return render(request, 'autores/autores_list.html', context)

# Como está esperando un id para mostrar la lista que corresponde, tiene que pasarse como parámetro.
def autor_detail(request, id):
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

    context = {
        "autor": None,
    }
    for autor in autores:
        if autor['id'] == id:
            context['autor'] = autor
            

    return render(request, 'autores/autor_detail.html', context)