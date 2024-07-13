from books.models import Autor

def run():
    print(Autor.objects.all())