import bs4
import requests

resultado = requests.get("https://escueladirecta.com/l/products?sortKey=name&sortDirection=asc&page=1")

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('img')[3]['src']
print(imagenes)

imagen_curso = requests.get(imagenes)
#print(imagen_curso.content)
 
f = open("mi_imagen.jpg", "wb")
f.write(imagen_curso.content)
f.close()