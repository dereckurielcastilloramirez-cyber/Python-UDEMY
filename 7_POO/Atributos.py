#-------------------------------ATRIBUTOS DE INSTANCIA----------------------------------

class Autos:

    def __init__(self, color, marca): #self, parametro
        #self.atributo = parametro
        self.color = color
        self.marca = marca

#crear objeto = asigna un atributo
mi_auto = Autos('gris', 'Pontiac') #Parametros de la funcion def que es color, el atributo de la instancia

    # objeto.atributo
print(f" mi auto es de marca {mi_auto.marca} y su color es {mi_auto.color}")


#--------------------------------ATRIBUTOS DE CLASE--------------------------------------

class Aviones:

    aeronave = True

    def __init__(self, modelo, marca): #self, parametro
        #self.atributo = parametro
        self.color = modelo
        self.marca = marca


#crear objeto = asigna un atributo
mi_avion = Aviones('747', 'Boeing') #Parametros de la funcion def que es color, el atributo de la instancia

    # objeto.atributo
print(Aviones.aeronave)

print(mi_avion.aeronave)