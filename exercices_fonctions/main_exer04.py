print("\n")

capital_initial = 100

# Ici on suppose que le chasseur n'a encore tué personnne.....

nbre_poule = 0
nbre_vache = 0
nbre_chien = 0
nbre_amis = 0

# Nombre victimes de manière générale
nombre_victime = int(input('Avez-vous combien de victime ?  : '))

# On commence par récuperer les victimes de manière explicite
nbre_poule = int(input("Combien de poules ? "))
nbre_vache = int(input("Combien de vache ? "))
nbre_chien = int(input("Combien de chien ? "))
nbre_amis = int(input("Combien d'amis ? "))


print("\n")
liste_victime = [nbre_poule,nbre_vache,nbre_chien,nbre_amis]
print(liste_victime)

total_victime = sum(liste_victime)
print(total_victime)

if total_victime > nombre_victime:
    print("Erreur La somme de vos victimes dépasse le nombre total de vos victimes que vous avez saisi au dépaart, prière de revenir au dessus")

else:
    #Ensuite nous pourrons recupérer le nombre exacte des points perdus et ce qui reste
    nbre_points_reste = (capital_initial - nbre_poule * 1 - nbre_vache * 5 - nbre_chien * 3 - nbre_amis *10) 
    nbre_points_perdus = capital_initial - nbre_points_reste
    
    print(f"Vous avez perdu {nbre_points_perdus} points et il vous en reste {nbre_points_reste} points.")

def amende(nombre_victime : int ) -> int :
    
    montant_payer = nombre_victime * 200
    
    return montant_payer

result = amende(nombre_victime)

print(f"Votre amende à payer est de {result} euros")