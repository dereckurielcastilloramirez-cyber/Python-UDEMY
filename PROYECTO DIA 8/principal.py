from generadores import numeros


def preguntar():
    print(" Bienvenido a tiendas PYTHON")

    

    while True:
        print("""
              [P] - PERFUMERIA
              [F] - FARMACIA
              [C] - COSMETICA
              """)
        try:
            departamento = input("Ingrese el departamento a visitar: ").upper()
            ["P", "F", "C"].index(departamento) # DEVUELVE SI HAY UN ERROR EN EL VALOR AL NO ENCONTRAR
        except ValueError:
            print("Esa no es una opcion Valida")
        else: 
            break

    numeros.decorador(departamento)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Desea sacar otro turno S / N: ").upper()
        except ValueError:
            print("Esa no es una opcion Valida")
        else:
            if otro_turno == "N":
                print("Gracias por visitarnos")
                break
            
inicio()