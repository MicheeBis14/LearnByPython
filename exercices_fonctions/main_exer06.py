from pathlib import Path

comptes = [ 
           
            {'nom': 'Boismoneau', 'prenom': 'stephane', 'epargne': 2500},
            {'nom': 'Jambon', 'prenom': 'fred', 'epargne': 5000},
            {'nom': 'Durois', 'prenom': 'nicolas', 'epargne': 10000},
            {'nom': 'Gueux', 'prenom': 'phillipe', 'epargne': 1250},
            {'nom': 'Duchan', 'prenom': 'alice', 'epargne': 4530},
            {'nom': 'Lepenou', 'prenom': 'amed', 'epargne': 2200},
            {'nom': 'Gueux', 'prenom': 'bernard'},
            {'nom': 'Jambon', 'prenom': 'steven', 'epargne': 1670},
            {'nom': 'Gueux', 'prenom': 'sylvie', 'epargne': 3},
            {'nom': 'Durois', 'prenom': 'berbard', 'epargne': 300000}
]



def get_result(comptes : list):

    
    for res in comptes:
        
        if res["nom"] == "Durois":
            print(res.get("epargne"))
            
get_result(comptes)
        

            
voie = Path.cwd()/"exercices_fonctions"/"main_exer08.py"
voie.touch(exist_ok=True)

if voie:
    print("Successs")
else:
    print("Sorryyyyyyyyyy")

# print(voie)
    


