
from pathlib import Path
import json
import shutil



employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
        }

#  ***********************-------------------------         ----------------------************************

# Patrick a quitté l'entreprise cette année, nous devons donc l'enlever du dictionnaire
# Julie a fêté son anniversaire hier, il faut donc changer son âge (elle a maintenant 26 ans).
# Paul quant à lui fêtera son anniversaire la semaine prochaine. Nous voulons donc récupérer son âge pour savoir quel âge il aura.
# Notre dictionnaire sera donc égal à la fin du script à :

    # employes = {
                # "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
                # "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 26}
                # }
    # Il faudra également récupérer l'âge de Paul dans une variable 'age_paul', qui devra donc être égale à 32.

# commençeons par supprimmer Patrick qui venait de  quitter l'entreprise

print('\n')
print('\n')
del employes["id03"]

#  On modifie maintenant l'age de Julie
employes["id02"]["age"] = 26

print("\n")

# on recupère l'age de Paul

age_paul = employes["id01"]["age"]

print(f"Paul a {age_paul} ans")

# On affiche le dictionnaire  
print(employes)


parnt = Path.cwd()
repertoire_tri_file = parnt/"repertoire_tri_file"
repertoire_tri_file.mkdir(exist_ok=True)

if repertoire_tri_file:
    print("dossier crée")

main_tri = repertoire_tri_file/"main_tri.py" 
main_tri.touch()

if main_tri:
    print('fichier crée')

