lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
#for nombre, indice in enumerate(lista_nombres):
#    print(f'{nombre} se encuentra en el índice {indice}')
#_-------------------------------------------------
python = "python"
lista = list(enumerate(python))
#print(lista)
#-------------------------------------------------
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for lugar, name in enumerate(lista_nombres):
    boole = lista_nombres[lugar].find("M")
    if boole != -1:
        print(f"{lugar} -> {name}")