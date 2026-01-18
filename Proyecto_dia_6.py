"""
Administrador de recetas

- ENCERRAR DENTRO DE UN WHILE HASTA QUE SEA LA OPCION 6 PARA SALIR
- LIMPIAR LA PANTALLA
- BUSCAR METODOS DE PATH
- CONCATENAR EN FUNCIONES
- DIAGRAMA DE FLUJO PARA VISUALIZAR PARA ARBOL DE DECISIONES

1. Bienvenida
2. Informar Ruta de acceso
3. Cuantas recetas hay en esa carpeta
4. dar opciones
    a. leer receta
        - elegir categoria
        - mostrar categoria
        - elegir receta
    b. crear receta
        - elegir categoria
        - crear nombre
        - crear contenido
    c. crear categoria
        - nombre de categoria
        - crear categoria
    d. eliminar receta
        - eliminar categoria
        - mostrar recetas
        - elegir receta
        - eliminar receta
    e. eliminar categoria
        - elegir categoria
        - eliminar categoria
    f. finalizar programa
        - finalizar ejecucion del codigo

"""
#importar modulos
import os
from pathlib import Path
from os import system
#Ruta de carpeta-------------------------------
mi_ruta = Path("M://UDEMY//Recetas")
#Contar recetas--------------------------------
def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

#MENU INICIO---------------------------------------------------------------------------
def inicio():
    system('cls')
    print('*' * 50)
    print('*' * 5 +" Bienvenido al administrador de recetas " + '*' * 5)
    print('*' *  50)
    print('\n')
    print(f"Las recetas estan en {mi_ruta}")
    print(f"Total de reetas: {contar_recetas(mi_ruta)}")

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion: ")
        print(''' 
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa
        ''')
        eleccion_menu = input("Opcion: ")
    return int(eleccion_menu)

# mostrar categorias------------------------------------------------------------------
def mostrar_categorias(ruta):
    print("Categorias: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador+=1
    
    return lista_categorias

# elegir categorias--------------------------------------------------------------------
def elegir_categorias(lista):
    eleccion_correcta = 'x'
    
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\n Elige una categoria: ")
    
    return lista[int(eleccion_correcta)-1]

#Mostrar recetas-----------------------------------------------------------------------
def mostrar_recetas(ruta):
    print("Recetas")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f'[{contador}] - {receta_str}')
        lista_recetas.append(receta)
        contador+=1
    
    return lista_recetas

# elegir recetas-------------------------------------------------------------------------
def elegir_recetas(lista):
    eleccion_receta = 'x'
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista)+1):
        eleccion_receta = input("\n Elige una receta: ")
    
    return lista[int(eleccion_receta)]

# Leer receta ...........................................................................
def leer_receta(receta):
    print(Path.read_text(receta))

# Crear receta---------------------------------------------------------------------------
def crear_receta(ruta):
    existe = False
    while not existe:
        nombre_receta = input("Escribe el nombre de tu receta: ") + '.txt'
        contenido_receta = input("Escribe tu nueva receta: ")
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f'Tu receta {nombre_receta} ha sido creada')
            existe = True
        else: 
            print("Lo siento, esa receta ya existe")

# Crear una categoria--------------------------------------------------------------------
def crear_categoria(ruta):
    existe = False
    while not existe:
        nombre_categoria = input("Escribe el nombre de la nueva categoria: ") + '.txt'
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'Tu caegoria {nombre_categoria} ha sido creada')
            existe = True
        else: 
            print("Lo siento, esa categoria ya existe")

# eliminar receta--------------------------------------------------------------------------
def eliminar_receta(receta):
    Path(receta).unlink()
    print(f'La receta {receta.name} ha sido eliminada')

#eliminar categoria------------------------------------------------------------------------
def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f'La categoria {categoria.name} ha sido eliminada')

# volver al inicio-------------------------------------------------------------------------
def volver_inicio():
    eleccion_regresar = "x"

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\n Presione v para volver al menú: ")
    
finalizar_programa = False

while not finalizar_programa:
    
    menu = inicio()

    if menu == 1:

        #FUNCION 1 mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)

        #FUNCION 2 elegir una categoria
        mi_categoria = elegir_categorias(mis_categorias)

        #FUNCION 3 mostrar recetas
        mis_recetas = mostrar_recetas(mi_categoria)

        #FUNCION 4 elegir receta
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        #FUNCION 5 leer la receta elegida
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_receta(mi_receta)
        #FUNCION 6 volver al inicio
        volver_inicio()

    elif menu == 2:
        #FUNCION 1 mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)

        #FUNCION 2 elegir una categoria
        mi_categoria = elegir_categorias(mis_categorias)

        #FUNCION 3 crear receta nueva
        crear_receta(mi_categoria)

        #FUNCION 6 volver al inicio
        volver_inicio()

    elif menu == 3:
        #FUNCION 7 crear categoria
        crear_categoria(mi_ruta)

        #FUNCION 6 volver al inicio
        volver_inicio()

    elif menu == 4: 
        #FUNCION 1 mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)

        #FUNCION 2 elegir una categoria
        mi_categoria = elegir_categorias(mis_categorias)

        #FUNCION 3 mostrar recetas
        mis_recetas = mostrar_recetas(mi_categoria)

        #FUNCION 4 elegir receta
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
       
        #FUNCION 8 eliminar receta      
        else:
            mi_receta = elegir_recetas(mis_recetas)
            eliminar_receta(mi_receta)

        #FUNCION 6 volver al inicio
        volver_inicio()
        
    elif menu == 5:

        #FUNCION 1 mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)

        #FUNCION 2 elegir una categoria
        mi_categoria = elegir_categorias(mis_categorias)
        
        #FUNCION 3 Eliminar categoria
        eliminar_categoria(mi_categoria)

        #FUNCION 6 volver al inicio
        volver_inicio()

    elif menu == 6:
        finalizar_programa = True


        pass