from django.shortcuts import render

# Create your views here.
def autores_view(request):
    return render(request, 'autores/autores_list.html')