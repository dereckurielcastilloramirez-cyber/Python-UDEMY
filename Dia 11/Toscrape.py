import bs4
import requests

url_base = "https://books.toscrape.com/catalogue/page-{}.html" # https://books.toscrape.com/catalogue/page-2.html
#print(url_base.format(1))
#for pagina in range(1,10):
    #print(url_base.format(pagina))

resultado = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#lista
libros = sopa.select('.product_pod') # selecciona todos los elementos con la clase product_pod de la pagina 1

ejemplo = libros[0].select('.star-rating.Three') # selecciona la clase del primer elemento con la clase star-rating y obtiene la segunda clase (la que indica la calificacion)
print(libros)

titulo = libros[0].select('a')[1]['title'] # extrae el titulo  elemento con la clase a
