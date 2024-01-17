import json
from pathlib import Path



michee = r"D:\Learning\Python\from_phaka\michee.json"
print(michee)

print('\n')

name = input("Entrez votre nom svp! : ")

post_name = input("Entrez votre postnom svp! : ")

first_name = input("Entrez votre prenom svp! : ")

notice = input("Donnez votre avis svp! : ")



with open (michee, "r" , encoding='utf-8') as f:
    
    data = json.load(f)
    
    datas = {"nom ": name, 
             "postnom ": post_name,
             "prenom": first_name,
             "avis": notice
        }
    
    
    data.append(datas)
    
    
        
with open (michee, "w", encoding='utf-8') as ff:
        database = json.dump(data, ff, indent= 4)
        
        if data:
            print('success')
            
        else:
            print('Error')