
#archivo = open('Archivo.txt', 'w')
#archivo.write('nuevo texto \n salto linea')
#archivo.write('''nuevo texto
# salto linea''')
#archivo.writelines(['Hola','mundo','1'])

#archivo.close()
#--------------------------------------------
#archivo = open('Archivo.txt', 'a')
#archivo.write(''' USO DE MODO >a< ''')
#
#archivo.close()
#------------------------------------------------
archivo = open('Archivo.txt','a')
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga \n"]
archivo.writelines('\t'.join(registro_ultima_sesion))

archivo = open('Archivo.txt','r')
print(archivo.readline())
archivo.close()