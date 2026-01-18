from random import *

aleatorio = randint(1,50)
#print(aleatorio)
aleatorio_1 = round(uniform(1,5),1)
#print(aleatorio_1)
r = random()
#print(r)
colores = ['azul','rojo','amarillo','verde']
aleatorio_2 = choice(colores)
#print(aleatorio_2)

lista = list(range(1,50,5))
print(lista)
shuffle(lista)
print(lista)