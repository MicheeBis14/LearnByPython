from pathlib import Path
voie = Path.cwd() /"creating_dos"

dossier1 = voie

print(dossier1)

dict_file = {
                "Films" : [
                    "Parker",
                    "Le Flingueur",
                    "ChasseHomme",
                    "Fiction" ],
                
                "Employes" : [
                    "Bisben",
                    "Kilolo",
                    "Phaka",
                    "Lola" 
                    ],
                "Cours" : [
                    "Staff",
                    "Macro",
                    "Econometrie",
                    "Python"
                    ]    
        }
# Dossier parent Films
(dossier1/"Films").mkdir(exist_ok=True)

# Dossier parent Employes
(dossier1/"Employes").mkdir(exist_ok=True)

# Dossier parent Cours
(dossier1/"Cours").mkdir(exist_ok=True)

# Parcourons le premier dossier parent parent Films 
for values in dict_file["Films"]:
    (dossier1/"Films"/values).mkdir(exist_ok=True)
    
# Parcourons Le deuxieme dossier parent Employes
        
for values in dict_file["Employes"]:
    (dossier1/"Employes"/values).mkdir(exist_ok=True)
    
# Parcourons le troisieme dossier parent Cours
    
for values in dict_file["Cours"]:
    (dossier1/"Cours"/values).mkdir(exist_ok=True)
    
    if values:
        print("Ok")
        
# for cle in dict_file:
#     (dossier1/cle).mkdir(exist_ok=True)
    
#     for values in dict_file["Films"]:
#         (dossier1/cle/values).mkdir(exist_ok=True)
        
#     for values in dict_file["Employes"]:
#         (dossier1/cle/values).mkdir(exist_ok=True)
    
#     for values in dict_file["Films"]:
#         (dossier1/cle/values).mkdir(exist_ok=True)
    
#     if cle:
#         print("Ok")