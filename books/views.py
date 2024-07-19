from django.shortcuts import render

# Create your views here.
def autores_view(request):
    return render(request, 'general/contact.html')

def libros_view(request):
    return render(request, 'general/contact.html')

def editoriales_view(request):
    return render(request, 'general/contact.html')