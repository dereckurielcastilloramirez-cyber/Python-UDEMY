def suma():
    n1 = int(input("N1 = "))
    n2 = int(input("N2 = "))

    print(n1+n2)
    print("Sumado " + n1)

try:
    #Codigo a probar
    suma()

#except:
    #Codigo a ejecutar si hay error
#    print("Algo no salio bien")

except ValueError:
    print("Error en el valor")

except TypeError:
    print("No concatenar string y enteros")

else:
    #Codigo a ejecutar si no hay error
    print("Hiciste todo bien")

finally: 
    #Codigo que se va a ejecutar de todos modos
    print("Eso fue todo")

