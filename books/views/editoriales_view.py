from django.shortcuts import render
from books.models import Editorial
from books.forms import EditorialCreate, EditorialModelFormCreate
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

def editoriales_view(request):
    editoriales = Editorial.objects.all()  # Obtén todos los objetos del modelo Editorial
    
    context = {
        "editoriales": editoriales,  # Contexto correcto
        "titulo": "Editoriales. Usando contexto."
    }
    
    return render(request, 'editoriales/editoriales_list.html', context)


def editorial_detail(request, id):
    '''
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
    '''
    
    editorial = get_object_or_404(Editorial, pk=id)
    
    context = {
        "editorial": editorial,
    }
        
    return render(request, 'editoriales/editorial_detail.html', context)


def editorial_create(request):
    if request.POST:
        form = EditorialModelFormCreate(request.POST)
        if form.is_valid():       
            nueva_editorial = form.save()
            
            '''
            nueva_editorial = Editorial.objects.create(
                nombre=form.cleaned_data['nombre'],
                direccion=form.cleaned_data['direccion'],
                ciudad=form.cleaned_data['ciudad'],
                estado=form.cleaned_data['estado'],
                pais=form.cleaned_data['pais'],
                codigo_postal=form.cleaned_data['codigo_postal'],
                telefono=form.cleaned_data['telefono'],
                email=form.cleaned_data['email'],
                sitio_web=form.cleaned_data['sitio_web'],
                fecha_fundacion=form.cleaned_data['fecha_fundacion'],
            )'''
            
            # Redireccionamos a al vista detalle de la editorial creada
            return redirect(reverse('books:editorial_detail', kwargs={'id': nueva_editorial.pk}))
    else: 
        form = EditorialCreate()
        
    context = {
        "form": form,
    }
        
    return render(request, 'editoriales/editorial_create.html',context=context)