nombre = int(input("entrezz un nombre : "))

compteur = 0

for i in range(1,nombre+1):
    if i % 2 == 0:
        compteur += 1
print(" 2 entre dans  " + str(nombre) + ",  " + str(compteur) + " fois ")