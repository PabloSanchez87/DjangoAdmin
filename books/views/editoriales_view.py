from django.shortcuts import render

from books.models import Editorial
# Create your views here.

def editoriales_view(request):
    
    # editoriales = [
    #   {
    #       "id": 1,
    #       "nombre": "Planeta"
    #   },
    #   {
    #       "id": 2,
    #       "nombre": "Disney"
    #   },
    #   {
    #       "id": 3,
    #       "nombre": "Espasa"
    #   },
    # ]
    
    editoriales = Editorial.objects.all()
    
    context = {
        "editoriales": editoriales,
        "titulo": "Editoriales. Usando contexto."
    }
    
    return render(request, 'editoriales/editoriales_list.html', context)

def editorial_detail(request, id):
    editoriales = [
      {
          "id": 1,
          "nombre": "Planeta"
      },
      {
          "id": 2,
          "nombre": "Disney"
      },
      {
          "id": 3,
          "nombre": "Espasa"
      },
    ]

    context = {
        "editorial": None,
    }
    for editorial in editoriales:
        if editorial['id'] == id:
            context['editorial'] = editorial
            break
        
    return render(request, 'editoriales/editorial_detail.html', context)
