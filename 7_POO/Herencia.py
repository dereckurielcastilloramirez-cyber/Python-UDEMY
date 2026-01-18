class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")
    

class Pajaro(Animal):
    
    pass

Pichi = Pajaro(3, 'blanco')
print(Pichi.color )
Pichi.nacer() #Lo heredó de animal

#print(Pajaro.__bases__)           #de quien hereda
#print(Animal.__subclasses__())    #a quien hereda

class Vehiculo:
    def acelerar(self):
        pass
    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass