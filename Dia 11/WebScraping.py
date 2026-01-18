import requests
import bs4

resultado = requests.get('https://www.python.org/downloads/release/python-3101/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

parrafo = sopa.select('p')[3].getText()
#print(parrafo)

columna_final = sopa.select('.options-bar')
for elemento in columna_final:
    print(elemento.getText())

#print(sopa.select('title')[0].getText())
#print(sopa.select('p'))