
great_number = 0
indice = 0
nombre = []

for i in range(1,6):

    nombre = int(input("Veuillez entrez le nombre numero " + str(i) + " : "))
    print("\n")
    print("Le nombre numero " + str(i) +" = " + str(nombre))

    if nombre > great_number:
        great_number = nombre
        indice = i

print('\n')
print("Le plus grand nombre entré est : " + str(great_number))
print("Le plus grand nombre a été saisi à la position numero : " + str(indice))

