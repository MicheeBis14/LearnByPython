from pathlib import Path



premier_list = []
second_list = []

# Saisie des elements pour la première liste et Traitement
print('\n')
print("***************************------------------------ PREMIERE liste ----------------------------**********************************")
print("***************************------------------------ PREMIERE liste ----------------------------**********************************")
print("\n")

# compteur =input("Voulez-vous saisir combien d'élement pour la première liste ?  ")
# for i in range(1,compteur+10)

a = int(input("Entrez le premier element : "))


if a == 0:
    print("Le premier élement de la liste doit être différent de 0 svp, prière de revoir")
    
else:

    b = int(input("Entrez le deuxième element : "))
    c = int(input("Entrez le troisième element : "))
    
premier_list.extend([a,b,c])
print(premier_list)

converge = int(f"{a}{b}{c}")

print(converge)

print("\n")
print("***************************------------------------ PREMIERE liste ----------------------------**********************************")
print("***************************------------------------ PREMIERE liste ----------------------------**********************************")

print('\n')

print("***************************------------------------ DEUXIEME liste ----------------------------**********************************")
print("***************************------------------------ DEUXIEME liste ----------------------------**********************************")

aa = int(input("Entrez le premier élement de la deuxième liste svp :  "))

if aa == 0:
    print("Le premier élement de la liste doit être différent de 0 svp, prière de revoir")

else:
    bb = int(input("Entrez le deuxième élement de la deuxième liste : "))
second_list.extend([aa,bb])
print(second_list)

converge_two = int(f"{aa}{bb}")
print(converge_two)





print("\n")
print("***************************------------------------ DEUXIEME liste ----------------------------**********************************")
print("***************************------------------------ DEUXIEME liste ----------------------------**********************************")


print("\n")
print("**********************------------------------ ADDITION DE DEUX LISTES ----------------------------*****************************")

var_added = converge + converge_two

print(f" L'addition des élements de deux listes nous donnnent  {var_added} ")

print("\n")

var_added_str = list(str(var_added))


print(var_added_str)

# for number in var_added_str:
#     trosieme_list = []
#     trosieme_list.extend([number]       
#     print(trosieme_list)
  
    