import zipfile
import os
import shutil

#-------------COMPRIMIR ARCHIVO--------------- 1
'''
mi_zip = zipfile.ZipFile('comprimido.zip', 'w')

mi_zip.write('texto.txt') #nombre de archivo a comprimir
mi_zip.write('texto2.txt') #nombre de archivo a comprimir

mi_zip.close()

print(f'Archivo comprimido en {os.getcwd()}')
'''
#-------------COMPRIMIR ARCHIVO--------------- 2
carpeta_origen = 'C://Users//derec//Documents//CarpetaSuperior' #ruta de la carpeta a comprimir
carpeta_destino = 'C://Users//derec//Documents//comprimido' #ruta de la carpeta destino
shutil.make_archive(carpeta_destino, 'zip', carpeta_origen) #crea el archivo comprimido

#-------------DESCOMPRIMIR ARCHIVO---------------
'''
mi_zip_ABIERTO = zipfile.ZipFile('comprimido.zip', 'r') #CONTIENE AL ARCHIVO COMPRIMIDO

mi_zip_ABIERTO.extractall() #EXTRAE TODOS LOS ARCHIVOS JUNTOS Y LOS DEJA AFUERA
'''
#-------------DESCOMPRIMIR ARCHIVO--------------- 2
shutil.unpack_archive('C://Users//derec//Documents//comprimido.zip', 'C://Users//derec//Documents//descomprimido', 'zip') #EXTRAE TODOS LOS ARCHIVOS JUNTOS Y LOS DEJA AFUERA