print('Practicas de PYTHON')
print("Practica No. " + input('Practica No: ') + " " + input('Nombre: '))

#CALCULADOR DE COMISION
#-tipos de datos ---> 
# string, "caracter"
# integer, 6,1,5
# float, 4.55, 3.40, 4.00
# lists, ["Sal", 5, -3, 0]
# dictionary, {'color': 'rojo', 'arte':'cine'}
# tuple, ('lun','mar', 'mie','jue', 'vie') --- orden no modificable
# set, {'a', 'b', 'c', 'd', 'e'} --- conjunto de elementos unicos, no se pueden repetir
# bool, True, False

#-variables

nombre = input("Cual es tu numbre: ")
ventas = float(input("Cual es el monto de ventas: "))

comision = ventas*(13/100)

print(f"OK {nombre}, tus ventas fueron {ventas} por lo que tu comision es {round(comision,2)}")
