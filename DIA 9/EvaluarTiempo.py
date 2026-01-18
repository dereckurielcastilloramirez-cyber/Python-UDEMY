import timeit




declaracion = '''
prueba_for(10)
'''
setup = '''
def  prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''


duracion = timeit.timeit(declaracion, setup, number=10000000)
print(f"FOR: {duracion}")

declaracion2 = '''
prueba_while(10)
'''
setup2 = '''
def prueba_while(numero):
    lista = []
    contador = 1

    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion2 = timeit.timeit(declaracion2, setup2, number=10000000)
print(f"while: {duracion2}")


"""
import time


def  prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1

    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

inicio = time.time()
prueba_for(100000)
final = time.time()
print(f"FOR: {final - inicio}")

inicio2 = time.time()
prueba_while(100000)
final2 = time.time()
print(F"WHILE:  + {final2 - inicio2}")

"""