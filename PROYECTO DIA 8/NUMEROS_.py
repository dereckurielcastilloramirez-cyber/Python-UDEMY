def decorador(departamento):
    print("\n" + "*" * 30)
    print("Su numero es: ")

    if departamento == 0:
        print(next(p))
    if departamento == 1:
        print(next(f))
    if departamento == 2:
        print(next(c))
        
    print("Aguarde  sera atendido")
    print("*" * 30 +"\n" )


def perfumeria():
    for turno_perfumeria in range(1,1000):
        yield f"P - {turno_perfumeria}"

def farmacia():
    for turno_farmacia in range(1,1000):
        yield f"F - {turno_farmacia}"
        
def cosmetica():
     for turno_cosmetica in range(1,1000):
        yield f"C - {turno_cosmetica}"

p = perfumeria()
f = farmacia()
c = cosmetica()

