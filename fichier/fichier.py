
way = "D:/Learning/Python/fichier/fichier.txt"

with open(way, "w", encoding='utf-8') as fichier:
    # contenu = fichier.read()
    # print(contenu)

    fichier.write("je suis egalement freelancer basé en design graphique bien evidemment")
    
with open(way, "a", encoding='utf-8') as ad_data:
    ad_data.write("\n kilolo bisben michee")
    
with open(way, "a", encoding='utf-8') as ad_data:
    ad_data.write("\n kestia ngombo nsita")
    
with open(way, "a", encoding='utf-8') as ad_data:
    ad_data.write("\n katika masala adel" )
    
    
    
with open(way , "r", encoding='utf-8') as newf:
    new_contenu = newf.read()
    
    print(new_contenu)
 
 