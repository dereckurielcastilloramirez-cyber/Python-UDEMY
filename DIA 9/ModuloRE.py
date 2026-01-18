# REGULAR EXPRESSIONs
import re

text = "Si necesitas ayuda, por favor, llama a un agente de soporte al 800-555-1234 las 24 horas del día."
"""
patron ='o'

busqueda = re.search(patron, text)
busqueda2 = re.findall(patron, text)

print(busqueda)
print(busqueda2)

for hallazgo in re.finditer(patron, text):
    print(hallazgo.span())

"""
#UBICACION
patron = r'\d\d\d-\d\d\d-\d\d\d\d'

resultado = re.search(patron, text)
print(resultado)

#grupo especial
pat = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(pat, text)
print(resultado.group(1))