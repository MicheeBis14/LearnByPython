from pathlib import Path
#  D:\Learning\Python\try_except\fichier_valid.txt
#  D:\Learning\Python\try_except\fichier_invalid.abc

print('\n')

try:
    fichier = input("Entrez le chemin du fichier svp ! :  ")
    
    with open(fichier, "r", encoding="utf-8") as file_open:
        
        data = file_open.read()
        
        print('\n')
        
        print(data)
        
except FileNotFoundError:
     print("Le fichier n'existe pas ou n'est pas trouvé, Desolé !!!")
     
except UnicodeDecodeError:
    print("Impossible d'ouvrir le fichier")

finally:
    print("Finn du script")