
suma = 0
for i in range(0,5):
    suma = suma + i*2
    if suma % 2 == 0:
        print(suma)
    else:
        continue
print("Fin")