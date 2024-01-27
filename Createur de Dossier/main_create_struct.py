from pathlib import Path

root_main = Path.cwd()/"Createur de Dossier"


dictionnaire_structure = {
                "Cours" : [
                    "Ecopolo", 
                    "Macro", 
                    "Econometrie", 
                    "STAFF"],
                
                "Films" : [
                    "Parker",
                    "Le Flingueur",
                    "Jason Darulo",
                    "La vie est belle"
                ],
                
                "Pays" : [
                    "USA",
                    "FRANCE",
                    "CANADA",
                    "BELGIQUE"
                ]
}

for item in dictionnaire_structure:
    (root_main/item).mkdir(exist_ok=True)
    
    
    if item:
        print('succès')
    
    
root_m = Path.cwd() / "organiser_data" /"file_prenoms.txt"
root_m.touch(exist_ok=True)