import re
"""
clave = input("Introduce tu clave: ")

#patron = r'\D{1}\w{7}'
revisar = re.search(patron, clave)

print(revisar)
"""

numero = input("Introduce tu numero: ")

#pat = r'\d{10}'

buscar = re.search(r'55|56', numero)
buscar2 = re.search(r'55..', numero)
b = re.search(r'^\d\d', numero)
print(b)
print(buscar)
print(buscar2)

