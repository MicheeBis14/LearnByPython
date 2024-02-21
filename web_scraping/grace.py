import json

chemin = r"D:\Learning\Python\web_scraping\from_web.json"


nom = input("votre nom : ? ")
postnom = input("votre postnom : ? ")
prenom = input('votre prenom svp : ')
telephone = input('votre numero de teephone svp : ')


with open("file.xlsx", "w", encoding='utf-8') as file_to_add:
    base_de_donnees = {
        "nom" : nom,
        "postnom" : postnom,
        "prenom" : prenom,
        "telephone" : telephone
    }
    bd = str(base_de_donnees)
    
    # json.dump(base_de_donnees, file_to_add, indent=5)
    file_to_add.write(bd)
    
    if base_de_donnees:
        print("sucess")
    else:
        print("erreurrrrr")