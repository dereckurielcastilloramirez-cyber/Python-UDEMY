import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

#crear BD
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}') ##leer imagen
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0]) # solo tomar el nombre sin el .jpg

print(nombres_empleados)

#codificar imagenes
def codificar_imagenes(imagenes):
    #lista 
    lista_codificada = []
    #imagenes a RGB
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        #codificar imagen
        codificado = fr.face_encodings(imagen)[0]

        #agregar a la lista
        lista_codificada.append(codificado)
    #devolver lista codificada
    return lista_codificada

def registrar_ingresos(persona):
    f = open('registro.csv', 'r+')
    lista_datos = f.readlines()

    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')#transformar a string
        f.writelines(f'\n{persona},{string_ahora}')

#almacenar codificaciones con RGB
lista_empleados_codificada = codificar_imagenes(mis_imagenes)

#tomar imagen de camara
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#leer imagen
exito, imagen = captura.read()

if not exito:
    print("No se pudo leer la imagen")
else:
    print("reconociendo...")
    #reconocer cara en captura
    cara_captura = fr.face_locations(imagen)

    #codificar cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    #coincidencias de captura y empleado
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif) #lista que almacena las distancias de la comparacion entre la imagen y la BD
        #print(distancias)

        indice_coincidencia = numpy.argmin(distancias) # indice en lista del minimo valor de distancia en una lista de distancias
        
        #mostrar coincidencia
        if distancias[indice_coincidencia] > 0.6:
            print("No coincide con ningun empleado")
        
        else:
            #buscar nombre empleado
            nombre = nombres_empleados[indice_coincidencia]

            #variables 
            y1, x2, y2, x1 =  caraubic #posiciones de la cara capturada
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)# rellenar en color verde
            cv2.putText(imagen, nombre, (x1 + 10, y2 - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            registrar_ingresos(nombre)

            #mostrar imagen obtenida
            cv2.imshow("imagen web", imagen)

            #mantener ventana abierta
            cv2.waitKey(0)

