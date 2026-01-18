
from random import randint

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
        
        def __init__(self, nombre, apellido, numero_cuenta, balance):
             super().__init__(nombre, apellido)
             self.numero_cuenta = numero_cuenta
             self.balance = balance
        
        def Imprimir_Cliente(self):
             
             print("Datos del cliente")
             print(f"\n Nombre: {self.nombre}")
             print(f"\n Apellido: {self.apellido}")
             print(f"\n Numero de Cuenta: {self.numero_cuenta}")
             print(f"\n Balance: {self.balance}")

        def Depositar(self):
             deposito = float(input("Ingrese la cantidad a depositar: "))
             self.balance = self.balance + deposito
             print(f"\n\tSu nuevo saldo es: ${self.balance}")
             
        
        def Retirar(self):
             retiro = float(input("Ingrese la cantidad a retirar: "))
             if retiro > self.balance:
                  print("Elija un monto valido")
             else:
                self.balance = self.balance - retiro
                print(f"\n\tSu nuevo saldo es: ${self.balance}")
        
        def Consultar(self):
             print(f"\n\tSu saldo actual es: ${self.balance}")

     
#----------------------PRINCIPAL-----------------------
def inicio():
     print(" ------------------ BIENVENIDO AL SISTEMA BANCARIO ----------------------- ")
     cliente = crear_cliente()
     
     print("\n -------------------------- MENU DE OPCIONES ----------------------- ")
     eleccion = 0
     while eleccion < 4:
          print("""
           1 - Depositar
           2 - Retirar
           3 - Consultar
           4 - Salir
           \n""")
          eleccion = int(input("Elija la opcion deseada: "))
          if eleccion == 1:
               cliente.Depositar()
          if eleccion == 2:
               cliente.Retirar()
          if eleccion == 3:
               cliente.Consultar()
     else:
          print(" ------------------------------ Cerrando sesion -----------------------------")


def crear_cliente():
     nombre = input("Ingrese su nombre: ")
     apellido = input("Ingrese su apellido: ")
     balance = float(input("Digite su saldo de apertura: "))
     cuenta = randint(1, 300000)
     cliente = Cliente(nombre, apellido, cuenta, balance)
     cliente.Imprimir_Cliente() 
     return cliente

inicio()