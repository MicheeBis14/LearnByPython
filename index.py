from pathlib import Path

# # nom = "Bonjour"

# # newnom = nom.replace("jour", "soir")

# # print(newnom)

# # postnom = "bisben kilolo"
# # newposst = postnom.title()

# # print (newposst)


# nome = "kilolobisbenmichee"

# nbr = nome.count('lo')
# print(nbr)

# chaine = "Pierre, Julien, Anne, Marie, Lucien"
# chaine_liste = chaine.split(", ")
# chaine_liste.sort()
# chaine_en_ordre = ", ".join(chaine_liste)

voie_mainn = Path.cwd()/"try_except"/"fichier_invalid.txt"
# voie_main.mkdir(exist_ok=True)
voie_mainn.touch(exist_ok=True)



if voie_mainn:
    print('ok')


