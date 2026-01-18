from collections import *
#counter --------------------------------------------

numeros = [8,2,5,3,2,4,7,8,1,9,4,5,6,4,3,1,7,9]

print(Counter(numeros))


FRASE = "Este es un ejemplo de frase"

print(Counter(FRASE))
print(Counter(FRASE.split()))

serie = Counter([1,2,3,4,5,6,7,8,9,10])
print(serie.most_common())

print(list(serie))

#defaultdict ----------------------------------------


dicc = defaultdict(lambda: 'nada')

dicc['uno'] = 'verde'
print(dicc['dos'])
print(dicc)

#namedtuple -----------------------------------------
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
dereck = Persona('Dereck', 1.70, 60)
print(dereck.altura)

# deque ----------------------------------------------

# Lista inicial de ciudades
ciudades_iniciales = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

# Crear la deque llamada lista_ciudades
lista_ciudades = deque(ciudades_iniciales)

# Mostrar la lista original
print("Lista original:")
print(lista_ciudades)

# Agregar elementos por la izquierda
lista_ciudades.appendleft("Ámsterdam")
lista_ciudades.append("Lisboa")

# Mostrar la lista actualizada
print("\nLista actualizada (con elementos agregados a la izquierda):")
print(lista_ciudades)
