import bs4
import requests

url_base = "https://books.toscrape.com/catalogue/page-{}.html" # https://books.toscrape.com/catalogue/page-2.html

#lista con Titulos ranqueados con 3 o más estrellas
titulos_ranqueados = []

#Iteración sobre todas las páginas
for pagina in range(1,51):
    
    #crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina) # obtiene el resultado de la pagina solicitada

    sopa = bs4.BeautifulSoup(resultado.text, 'lxml') # crear sopa

    #Seleccionar los datos de los libros de la pagina
    libros = sopa.select('.product_pod') # selecciona todos los elementos con la clase product_pod de la pagina 1

    #Iteración sobre los libros
    for libro in libros:
        
        #Revisar la calificación de cada libro de 4 o más estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0: 

            #Extraer el título del libro y Guardarlo 
            titulo_libro = libro.select('a')[1]['title']

            #Guardar el título en la lista
            titulos_ranqueados.append(titulo_libro)

#Imprimir los títulos de los libros ranqueados de 4 a 5 estrellas
i=0
for t in titulos_ranqueados:
    i+=1
    print(f"{i} - {t}")



