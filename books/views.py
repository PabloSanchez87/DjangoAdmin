from django.shortcuts import render

# Create your views here.
def autores_view(request):
    return render(request, 'autores/autores_list.html')

def libros_view(request):
    return render(request, 'libros/libros_list.html')

def editoriales_view(request):
    return render(request, 'editoriales/editoriales_list.html')