capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

frase = list(zip(paises,capitales))
#for p,c in frase:
#    print(f"La capital de {p} es {c}")

#_------------------------------------------------------
esp = ['uno','dos','tres','cuatro','cinco']
port = ['um', 'dois', 'três', 'quatro', 'cinco']
ing = ['one', 'two', 'three', 'four', 'five']

signif = list(zip(esp, port,ing))
N=0 
for e,p,i in signif:
    N += 1
    print(f"{N}: {e} - {p} - {i}")
