from pathlib import Path
import json
import shutil

dossier_parent_grace = Path.cwd()
creat_file = dossier_parent_grace/"grace_exer_non_res"/"file_json_for_grace.json"
creat_file.touch()

# if creat_file:
#     print("success")

print("\n")
print('---------------------******************** YOUR PROGRAM **********************--------------------')
print('\n')

nom_user = input("QUEL EST VOTRE NOM SVP ! : ").upper()
firstnom_user = input("QUEL EST VOTRE PRENOM PLEASE : ").upper()
second_nom_user = input("QUEL EST VOTRE POSTNOM PLEASE : ").upper()
sexe = input('VOTRE SEXE, MASCULIN ou FEMININ ? : ').upper()
age = input("ET VOTRE AGE SVP ").upper()
avice = input("QUELLE EST VOTRE IMPRESSION ").title()

my_way_file = creat_file

with open(my_way_file, "r", encoding='utf-8') as file_content:
    data = json.load(file_content)
     
    new_datas = {
            "nom_user" : nom_user,
            "firstnam_user " : firstnom_user,
            "second_name_user " : second_nom_user,
            "sexe " : sexe,
            "age " : age + " ans ",
            "votre_avis " : avice
        }
            
    data.append(new_datas)
    
    

with open(my_way_file, "w", encoding='utf-8') as file_add:
    data__add = json.dump(data,file_add, indent=4)

    if data:
        print(f" Votre fichier contenant les élements suivants : {data} a été actualisé avec succès ")
    else:
        print("Vous avez commis une erreur quelque part, priere de revoir votre code")
        