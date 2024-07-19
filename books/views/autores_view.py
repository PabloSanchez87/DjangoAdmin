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
        "titulo": "Prueba de paso de contexto"
    }
    
    
    return render(request, 'autores/autores_list.html', context)