nombre = int(input(" Entrez un entier strictement positif  : "))
div = 0

if nombre > 0:
    # i=2
    for  i in range(2,nombre):
         
        if nombre % i != 0:
            print(" Diviseurs propres sans répétition de : " + str(nombre) + " sont aucun, D'ou " + str(nombre) + " est premier" )  
        else:
            print('cest pas premier')
else:
    print("Veuillez entrer un entier positif ")

