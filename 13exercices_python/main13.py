#  Initialisation par 0 de la plus grande valeur et de l'indice
great_number = 0
indice = 0

# Ici j'au utilisé la boucle while qui va se repéter jusqu_à ce que l'utilisateur saissira 0 
while True:
    nombre = int(input("Veuillez saisir un nombre  numero " + str(indice) + " ou Zero si vous voulez arreter le programme.) : "))
    
    if nombre == 0:
        break
    indice += 1

    # Ici Je compare les nombres saisis par l'utilisateur et celui qu'on avait initialisé tout au début du script
    if nombre > great_number:
        great_number = nombre
        
        indice_great = indice

# Ici, Quand L'utilsateur introduit 0, je commence par vérifier si si au moins un nombre a été saisi sinon j'affiche qu'aucun nombre n'a été saisi.
if indice > 0:
    print("\n Le plus grand de ces nombres est :", great_number)
    print("C'était le nombre numero", indice_great)
else:
    print("Prière de saisir un nombre car Vous n'en avez saisi aucun jusque-là")