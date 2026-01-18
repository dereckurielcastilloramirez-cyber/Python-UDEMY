# FUNCIONES GENERADORAS CON YIELD
def perfumeria():
    for turno_perfumeria in range(1,1000):
        yield f"P - {turno_perfumeria}"

def farmacia():
    for turno_farmacia in range(1,1000):
        yield f"F - {turno_farmacia}"
        
def cosmetica():
     for turno_cosmetica in range(1,1000):
        yield f"C - {turno_cosmetica}"
    
#VARIABLES QUE LLAMAN A FUNCIONES
p = perfumeria()
f = farmacia()
c = cosmetica()
# DECORADOR QUE LLAMA A FUNCIONES (DEPARTAMENTO) QUE ES SU ARGUMENTO 

def decorador(departamento):
    print("\n" + "*" * 23)
    print("Su numero es: ")
    if departamento == "P":
        print(next(p))
    if departamento == "F":
        print(next(f))
    if departamento == "C":
        print(next(c))
    
    print("Aguarde  sera atendido")
    print("*" * 23 +"\n" )
       
                
        
