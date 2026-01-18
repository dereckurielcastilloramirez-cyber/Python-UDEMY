a=0
b=1
c=0

contador = 0
while contador < 10:
    print(a)
    c=a+b 
    a=b
    b=c
    contador = contador + 1

print("Fin del ciclo")