from random import *
Numero = int(input("Ingresa el numero: "))
Num_aleatorio = randint(1,100)
Error=0
while Error < 8:
    Error+=1
    if Numero<0 or Numero>100:
        print("Numero fuera de rango")
    elif Numero < Num_aleatorio:
        print("El numero es menor al elegido")
    elif Numero > Num_aleatorio:
        print("El numero es mayor al elegido")
    else:
        print(f"El numero es correcto, has adivinado en {Error} intentos")
        break
    Numero = int(input("Ingresa el numero: "))
print(f"Fin del juego, el numero era {Num_aleatorio}")

dic = {'clave1':300}
dic