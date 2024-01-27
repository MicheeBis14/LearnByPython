from pathlib import Path

print("\n")

# Chemine de mon fichier 
# root = Path.cwd() /"organiser_data" / "file_prenoms.txt"
# root_new = Path.cwd()/"organiser_data" / "prenom_final.txt"

root = r"D:\Learning\Python\organiser_data\prenoms.txt"
root_new = r"D:\Learning\Python\organiser_data\prenoms_final.txt"

# Ouverture du fichier

with open (root, "r", encoding='utf-8') as res_data:
    datas = res_data.read().splitlines()
    
prenoms_fan = []
    
for data in datas:
    prenoms_fan.extend(data.split())

# all_prenom = root/"all_prenom.txt"
# all_prenom.mkdir(exist_ok=True)

all_prenom = [prenom.strip(",. ") for prenom in prenoms_fan]


with open (root_new, "w", encoding='utf-8') as new_add:
    
    new_add.write("\n".join(sorted(all_prenom)))
    
    
    if all_prenom:
        print(True)
        
    else:
        print(False)
        

# with open (root_new, "r", encoding='utf-8') as new_load:
    
#     new_load.read().splitl

