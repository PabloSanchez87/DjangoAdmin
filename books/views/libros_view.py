from django.shortcuts import render

# Create your views here.
def libros_view(request):
    return render(request, 'libros/libros_list.html')
