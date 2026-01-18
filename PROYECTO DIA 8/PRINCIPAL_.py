import NUMEROS_

while True:
    print("""
              [0] - PERFUMERIA
              [1] - FARMACIA
              [2] - COSMETICA
              [3] - SALIR
              """)
    try:
        departamento = int(input("Digite su eleccion: "))
        [0, 1, 2, 3].index(departamento) # DEVUELVE SI HAY UN ERROR EN EL VALOR AL NO ENCONTRAR

    except ValueError:
        print("Esa no es una opcion Valida")

    else:
        if departamento == 3:
            print("Gracias por visitarnos")
            break
        NUMEROS_.decorador(departamento)