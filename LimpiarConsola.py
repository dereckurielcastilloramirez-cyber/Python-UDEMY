from os import system

nombre = input("Nombre: ")
edad = input("Edad: ")

system('cls')

print(f"Tu nombre es {nombre} y tienes {edad} años")


def registro_error(ruta):
    with open(ruta, 'a', encoding='utf-8') as archivo:
        archivo.write("se ha registrado un error de ejecución\n")
    return "Error registrado con éxito."

# Ejemplo con un archivo al que sí tengas acceso:
ruta = 'E:\\UDEMY\\PYTHON\\mi_archivo.txt'
resultado = registro_error(ruta)
print(resultado)
