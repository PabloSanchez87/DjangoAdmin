from django.shortcuts import render

# Create your views here.
def autores_view(request):     
    ## Muestra de como pasarle datos a nuestra vista.
    # Podemos verlo con debug_tools en la pestaña plantilla.
    autores = [
      {
          "id": 1,
          "nombre": "Antonio"
      },
      {
          "id": 2,
          "nombre": "Felipe"
      },
      {
          "id": 3,
          "nombre": "Matilde"
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
          "nombre": "Antonio"
      },
      {
          "id": 2,
          "nombre": "Felipe"
      },
      {
          "id": 3,
          "nombre": "Matilde"
      },
    ]

    context = {
        "autor": None,
    }
    for autor in autores:
        if autor['id'] == id:
            context['autor'] = autor

    return render(request, 'autores/autor_detail.html', context)