class Automoviles:
    
    motorizaccion = True

    def __init__(self, color, tipo):
        self.color = color
        self.tipo = tipo
    
# metodo de instancia-----------------------------------------------------------
    def marca(self):
        print("TESLA")
    

    def submarca(self, sub):
        print(f'El vehiculo {sub} es: ')
        self.marca()


    def modelo(self):
        self.color = 'Negro'
        print(f'el vehiculo TESLA es {self.color}')

#mi_auto = Automoviles("Gris", "Electrico")
    
#metodo de clase-----------------------------------------------------------------
    @classmethod
    def velocidad_maxima(cls, motor):
        print(f'La velocidad maxima para el {motor} es de 300km/h')
        cls.motorizaccion = False
        print(Automoviles.motorizaccion)

#Automoviles.velocidad_maxima("V6")

#metodo estatico ----------------------------------------------------------------

    @staticmethod
    def correr():
        print("El auto corre muy rapido")
#Automoviles.correr()