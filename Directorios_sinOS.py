#Windows
import os

archivo = open('E:\\UDEMY\\PYTHON\\Archivo.txt')
print(archivo.read())

# Mac y windows
from pathlib import Path

carpeta = Path('E:/UDEMY/PYTHON')
archivo_2 = carpeta / 'Archivo.txt'

mi_archivo = open(archivo_2)
print(mi_archivo.read())