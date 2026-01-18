mi_archivo = open('Archivo.txt')

#print(mi_archivo.read())

linea = mi_archivo.readline()
print(linea.upper())

linea = mi_archivo.readline()
print(linea.rstrip())

linea = mi_archivo.readline()
print(linea)

mi_archivo.close()


