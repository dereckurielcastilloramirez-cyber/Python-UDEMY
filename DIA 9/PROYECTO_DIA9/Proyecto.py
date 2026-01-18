import os
import re
import time
import datetime
import math

# Ruta de búsqueda
ruta = "C://Users//derec//Proyecto Dia 9//Mi_Gran_Directorio"

# Patrón de número de serie
patron = r"N[a-zA-Z]{3}-\d{5}"

# Fecha de búsqueda
fecha = datetime.datetime.now().strftime("%d/%m/%Y")

# Encabezado
print("-" * 60)
print(f"Fecha de búsqueda: {fecha}\n")
print("ARCHIVO\t\tNRO. SERIE")
print("-------\t\t----------")

# Contadores y tiempo de inicio
contador = 0
inicio = time.time()

# Recorrer carpetas y archivos
for carpeta, subcarpetas, archivos in os.walk(ruta):
    for archivo in archivos:
        if archivo.endswith(".txt"):
            ruta_completa = os.path.join(carpeta, archivo) # concatena ruta con nombre del archivo

            #f = open(ruta_completa, "r", encoding="utf-8")
            #contenido = f.read()
            #f.close()

            with open(ruta_completa, "r") as f: #abre y cierra el archivo de manera segura o open(ruta_completa, "r", encoding="utf-8")
                contenido = f.read()                      #lee el archivo y guarda en contenido
                encontrado = re.search(patron, contenido) #busca el patron en el contenido
                if encontrado:
                    print(f"{archivo}\t{encontrado.group()}")
                    contador += 1

# Tiempo final
final = time.time()
duracion = math.ceil(final - inicio)

# Resumen
print(f"\nNúmeros encontrados: {contador}")
print(f"Duración de la búsqueda: {duracion} segundos")
print("-" * 60)
