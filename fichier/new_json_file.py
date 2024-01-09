import json

voie = r"D:\Learning\Python\fichier\fichier.json"

with open(voie, 'w' , encoding='utf-8') as new_file_jsonn:
    json.dump('Bonjour Grace', new_file_jsonn)

with open(voie, 'r') as new_fil:
    result_file_json = json.load(new_fil)
    
    print(result_file_json)
# print(voie)

