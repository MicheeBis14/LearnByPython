print("Bienvenu, Soyez à l'aise rien ne pourra vous tuer ici")
print('\n')

# L'utilsateur saisi un nombre qu'on recupere dans une variable nombre_a 
nombre = input("Veuillez saisir un nombre : ")
nombre_converti = int(nombre)

print("Les nombres impaires allant de 0 à " + nombre, "sont respectivement : ")

for i in range(0, nombre_converti+1):
    if i % 2 != 0:
        print(i)


 