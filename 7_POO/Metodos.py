class Automoviles:
    
    funciona = True

    def __init__(self, color, marca):
        self.color = color
        self.marca = marca
    
    def velocidad(self):# sin argumentos
        print(f"velocidad de 100 km/h para el {self.marca}")

    def motor(self, version): #con argumentos
        print(f"El motor es 1.4 L para la version {version} ")

auto = Automoviles("Gris","Pontiac")
auto.funciona
auto.velocidad()
auto.motor("Comfortline")