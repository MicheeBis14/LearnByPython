from pathlib import Path

chemin_prenoms_file = r"D:\Learning\Python\organiser_data\prenoms.txt"
chemin_prenoms_final = r"D:\Learning\Python\organiser_data\prenoms_final.txt"

with open(chemin_prenoms_file, "r") as f:
    lines = f.read().splitlines()

prenoms = []

for line in lines:
    prenoms.extend(line.split())

prenoms_final = [prenom.strip(",. ") for prenom in prenoms]

with open(chemin_prenoms_final, "w") as f:
    f.write("\n".join(sorted(prenoms_final)))
    
    
    # main_road = Path.cwd() /"fonctions" / "main_function.py"
    
    # main_road.touch(exist_ok=True)
    
    # if main_road:
    #     print(True)
    # else:
    #     print(False)