import os
R = 'E:\\UDEMY\\PYTHON'
#es la ruta actual--------------------
ruta = os.getcwd()
#ruta nueva en carpeta diferente----------------------
ruta = os.chdir('E:\\UDEMY\\PYTHON')
#ya dentro de carpeta, abrir el archivo....
archivo = open('Archivo.txt')
#print(archivo.read())
#crear directorios o carpeta en esa ubicacion con su nombre al final
#ruta1 = os.makedirs('E:\\UDEMY\\PYTHON\\nuevo_archivo')

elemento = os.path.basename(R)
#print(elemento)

directorio = os.path.dirname(R)
#print(directorio)
#coloca en tupla directorio, elemento
separador = os.path.split(R)
#print(separador)

#eliminar carpeta
os.rmdir('E:\\UDEMY\\PYTHON\\nuevo_archivo')

