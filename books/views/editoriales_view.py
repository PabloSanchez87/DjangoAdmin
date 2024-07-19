from django.shortcuts import render

# Create your views here.

def editoriales_view(request):
    return render(request, 'editoriales/editoriales_list.html')