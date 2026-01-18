
lista_numero = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
n_pares = []
n_impares = []
suma_pares = 0
suma_impares = 0

for numero in lista_numero:
    if numero % 2 == 0:
        n_pares.append(numero)
        suma_pares = suma_pares + numero
    else:
        n_impares.append(numero)
        suma_impares = suma_impares + numero

print(f"Los pares: {n_pares}")
print(f"La suma es: {suma_pares}")
print(f"Los impares: {n_impares}")
print(f"La suma es: {suma_impares}")