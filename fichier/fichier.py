from pathlib import Path



disk_parent = Path.cwd().parent

new_dossier = disk_parent/"python"/"grace_exer_non_res"
new_dossier.mkdir(exist_ok=True)

print(new_dossier)

new_file = new_dossier/"main.py"
new_file.touch()

if new_file:
    print("succèss")
    
    # creation de notre premier fichier du repertoire grace_exer_non_res
    

    # new_file.touch(exist_ok=True)
    

# way = "D:/Learning/Python/fichier/fichier.txt"
# way = "D:\Learning\Python\fichier\fichier.txt"

# with open(way, "w", encoding='utf-8') as fichier:
    # contenu = fichier.read()
    # print(contenu)

    # fichier.write("je suis egalement freelancer basé en design graphique bien evidemment")
    
# with open(way, "a", encoding='utf-8') as ad_data:
#     ad_data.write("\n kilolo bisben michee")
    
# with open(way, "a", encoding='utf-8') as ad_data:
#     ad_data.write("\n kestia ngombo nsita")
    
# with open(way, "a", encoding='utf-8') as ad_data:
#     ad_data.write("\n katika masala adel" )
    
    
    
# with open(way , "r", encoding='utf-8') as newf:
#     new_contenu = newf.read()
    
#     print(new_contenu)
 
 