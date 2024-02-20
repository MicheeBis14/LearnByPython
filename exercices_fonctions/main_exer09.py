# Liste contenant les entiers 
print("\n")

print("*************************************---------------------- TRAITEMENT ------------------------***************************************")
print("*************************************---------------------- TRAITEMENT ------------------------***************************************")
print("\n")

# for i in range(6):
    
#     liste_gen  = []
#     print("Saisie des élements de la liste !!! ")
#     print("\n")
    
#     element = [int(input(f"Entrez l'élement n°{i} :  "))]
#     liste_gen.append(element)
    
# print(liste_gen)
    
    
liste_gen = [-2,-1,2,1]
cible =int(input("veuillez entrez votre cible svp "))


def somme_indice(liste_gen : list,  cible : int):
    
    """_summary_

    Args:
        liste_gen (list): Cette liste contient tous les élements que nous voulons parcourir afin de récuperer les différents 
        couples cible (int): Grace à cette variable, l'utilisateur va lui-même fournir à la fonctioon son élement ciblé
        
    Return:
        il s'agit d'écrire une fonction qui renvoie les couples des indices d'éléments de la liste(liste_gen), de telle sorte que
        la somme de ces deux éléments est égale à la valeur cible choisie.
    """
    
    liste_final = []
    size_list = len(liste_gen)
    
    
    for i in range(size_list):
        for j in range(i+1, size_list):
            
            if liste_gen[i] + liste_gen[j] == cible:
                liste_final.extend((i,j))
                
                # print(liste_final)
                return liste_final
                
                break
            else:
                print(f" Nous n'avons trouvé aucun couple dont leur somme est égal à la valeur du cible que vous avez saisi. Par conséquent la liste est vide {liste_final}")
                # break0
                
        
        
res = somme_indice(liste_gen,cible)   
print(res)              