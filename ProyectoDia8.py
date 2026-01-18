def generador_turnos(turno):
    turno_perfumeria = 0
    turno_farmacia = 0
    turno_cosmetica = 0

    if turno == 1:
        turno_perfumeria += 1
        yield  turno_perfumeria
    if turno == 2:
        turno_farmacia += 1
        yield  turno_farmacia
    if turno == 3:
        turno_cosmetica += 1
        yield  turno_cosmetica

print("""
                  DEPARTAMENTOS
      1 - PERFUMERIA        3 - COSMETICA
      2 - FARMACIA          4 - SALIR DE TURNOS
      
""")
turno = 1
while(turno>0 and turno<5):
    turno = int(input("Ingrese a que departamento acudira: "))
    if(turno == 4):
        break
    numeroTurno = generador_turnos(turno)
    print(f"Turno {next(numeroTurno)}")

else:
    print("Ingrese una opcion valida")
    