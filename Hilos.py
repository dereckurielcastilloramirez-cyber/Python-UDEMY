import threading
import time

def tarea(nombre):
    for i in range(3):
        print(f"Hilo {nombre} → iteración {i}")
        time.sleep(1)

# Crear hilos
hilo1 = threading.Thread(target=tarea, args=("A",)) #target=mi_funcion → significa "cuando inicie este hilo, corre esta función".
hilo2 = threading.Thread(target=tarea, args=("B",))

# Iniciar hilos
hilo1.start() #empieza a ejecutar la función correspondiente al hilo
hilo2.start()

# Esperar a que terminen
hilo1.join() #join() → espera a que el hilo termine antes de continuar con el siguiente código
hilo2.join()

print("¡Todos los hilos terminaron!")
