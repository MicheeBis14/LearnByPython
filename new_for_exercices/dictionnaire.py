from pathlib  import Path
import shutil


new_dictionnaire = {
    "nom" : "Kilolo",
    "postnom": "bisben",
    "prenom" : "michee",
    "sexe": "masculin",
    "promotion":"licence"
    
}

# result_dic = new_dictionnaire["nom"]
# print(result_dic)


    
dossier_par = Path.cwd()
    
create_file_employes = dossier_par/"new_for_exercices"/"employes_dict.py"
create_file_employes.touch(exist_ok=True)
    
if  create_file_employes:
    print('Fichier crée avec succès')
    
    
    
    
    