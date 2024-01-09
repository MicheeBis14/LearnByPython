import json 

voie = r"D:\Learning\Python\fichier\fichier_2.json"
# print(voie) 


with open(voie, 'w', encoding='utf-8') as new_data:
    json.dump(list(range(20)), new_data,indent=5)
    
    
with open(voie, 'r', encoding='utf-8') as new_dat:
    data = json.load(new_dat)
    
    data.append("bisben")
    
    
    
    

    
    