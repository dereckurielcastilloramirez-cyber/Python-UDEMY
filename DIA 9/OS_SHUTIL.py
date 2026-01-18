import os
import shutil
import send2trash
"""print(os.getcwd())

archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()

print(os.listdir())

"""

# shutil.move('curso.txt', "C:\\Users\\dereck\\Documents") # Mueve el archivo 

#send2trash.send2trash('curso.txt') # Elimina el archivo y manda a la papelera

ruta = 'C:\\Users\\derec\\Documents\\CarpetaSuperior'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la ruta {carpeta} encontramos:')
    for sub in subcarpeta:
        print(f'\t {sub}')
    print("Los archivos son:")
    for ar in archivo:
        print(f'\t {ar}')
    print('\n')
