texto1 = input("Ingrese texto: ")
texto = texto1.lower()
letras = []

letras.append(input("Letra 1: ").lower()) #los agrega en orden de la lista y los transforma en minusculas
letras.append(input("Letra 2: ").lower())
letras.append(input("Letra 3: ").lower())

n1 = texto.count(letras[0]) #cuenta cuantas veces aparece la letra en el texto
n2 = texto.count(letras[1])
n3 = texto.count(letras[2])

print(f"La letra '{letras[0]}' aparece {n1}")
print(f"La letra '{letras[1]}' aparece {n2}")
print(f"La letra '{letras[2]}' aparece {n3}")

palabras = texto.split() #separa el texto en partes y guarda en una lista nb 
num_pal = len(palabras) 
print(f"Hay {num_pal} palabras en el texto")

print(f"La primer letra es {texto[0]} y la ultima letra es {texto[-1]}")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"El texto invertido es:  {texto_invertido}")
python = "python" in texto
if python == True:
    print("La palabra 'python' si esta en el texto")
else:
    print("La palabra 'python' no esta en el texto")