from books.models import Editorial, Autor, Libro  # Importa los modelos necesarios desde la aplicación books
from datetime import date  # Importa la clase date para manejar fechas
import random  # Importa el módulo random para seleccionar autores aleatoriamente

# Creación de una lista de editoriales
editoriales = [
    Editorial(
        nombre=f'Editorial {i}',  # Nombre de la editorial
        direccion=f'Dirección {i}',  # Dirección de la editorial
        ciudad='Ciudad',  # Ciudad de la editorial
        estado='Estado',  # Estado de la editorial
        pais='País',  # País de la editorial
        codigo_postal=f'0000{i}',  # Código postal de la editorial
        telefono=f'123456789{i}',  # Teléfono de la editorial
        email=f'editorial{i}@example.com',  # Email de la editorial
        sitio_web=f'http://editorial{i}.com',  # Sitio web de la editorial
        fecha_fundacion=date(2000+i, 1, 1)  # Fecha de fundación de la editorial
    )
    for i in range(1, 11)  # Itera desde 1 hasta 10 para crear 10 editoriales
]

# Inserta todas las editoriales creadas en la base de datos de una vez para mayor eficiencia
Editorial.objects.bulk_create(editoriales)

# Creación de una lista de autores
autores = [
    Autor(
        nombre=f'Nombre {i}',  # Nombre del autor
        apellido=f'Apellido {i}',  # Apellido del autor
        fecha_nacimiento=date(1970+i, 1, 1),  # Fecha de nacimiento del autor
        nacionalidad='Nacionalidad',  # Nacionalidad del autor
        biografia=f'Biografía del autor {i}',  # Biografía del autor
        email=f'autor{i}@example.com',  # Email del autor
        telefono=f'987654321{i}',  # Teléfono del autor
        sitio_web=f'http://autor{i}.com',  # Sitio web del autor
        premios=f'Premio {i}'  # Premios recibidos por el autor
    )
    for i in range(1, 11)  # Itera desde 1 hasta 10 para crear 10 autores
]

# Inserta todos los autores creados en la base de datos de una vez para mayor eficiencia
Autor.objects.bulk_create(autores)

# Obtiene todas las editoriales y autores de la base de datos
editoriales = Editorial.objects.all()
autores = Autor.objects.all()

# Creación de una lista de libros
libros = [
    Libro(
        titulo=f'Título del Libro {i}',  # Título del libro
        isbn=f'123456789012{i}',  # ISBN del libro
        fecha_publicacion=date(2010+i, 1, 1),  # Fecha de publicación del libro
        numero_paginas=100+i,  # Número de páginas del libro
        idioma='Idioma',  # Idioma del libro
        descripcion=f'Descripción del libro {i}',  # Descripción del libro
        editorial=editoriales[i % len(editoriales)],  # Editorial del libro, asignada cíclicamente
        genero='Género',  # Género del libro
        precio=19.99 + i  # Precio del libro
    )
    for i in range(1, 11)  # Itera desde 1 hasta 10 para crear 10 libros
]

# Inserta todos los libros creados en la base de datos de una vez para mayor eficiencia
Libro.objects.bulk_create(libros)

# Asigna autores aleatoriamente a cada libro
for libro in Libro.objects.all():
    libro.autores.add(Autor.objects.get(pk=random.randint(1, Autor.objects.count())))  # Asigna un autor aleatorio
    libro.autores.add(Autor.objects.get(pk=random.randint(1, Autor.objects.count())))  # Asigna un segundo autor aleatorio
    libro.autores.add(Autor.objects.get(pk=random.randint(1, Autor.objects.count())))  # Asigna un tercer autor aleatorio
    libro.save()  # Guarda los cambios en el libro
