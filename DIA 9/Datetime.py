from datetime import *
"""
hora = datetime.time(17, 35)
dia = datetime.date(2025, 8, 8)

print(type(hora))
print(hora.minute) 

print(type(dia))
print(dia)

com = datetime.date(2025, 8, 8)
print(com.ctime())

from datetime import datetime

date = datetime(2025, 8, 8, 17, 35, 0)
print(date)

date = date.replace(year=2002, month=8, day=8)

print(date)
"""
#--------------------------------------------------

nacimiento = date(1962, 2, 21)
print(nacimiento)

defuncion = date(2012, 11, 17)
print(defuncion)

print((nacimiento - defuncion)/365)

hoy = date.today()
print(hoy)

# Obtener la hora actual
ahora = datetime.now()

# Extraer solo los minutos
minutos = ahora.minute

print(minutos)
