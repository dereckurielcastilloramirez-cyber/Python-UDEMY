class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")
    def hablar(self):
        print("Sonido")
    

class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        
        super().__init__(edad, color)  #Todas las asignaciones heredadas
    #   self.edad = edad
    #   self.color = color
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("Pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")
    
     

#Pichi = Pajaro(3, 'blanco', 50)
#mi_animal = Animal(5, 'negro')
#Pichi.volar(100)
#------------------------------------------------------------------------------------
class Padre:
    def hablar(self):
        print("Hola")
    pass

class Madre:
    def reir(self):
        print("Jajaja")
    def hablar(self):
        print("Que tal")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()