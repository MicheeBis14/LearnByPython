from pathlib import Path
import shutil

p = Path.cwd()
# print(p)

disk_d = p.parent.parent

disk_d_parcours = disk_d / "Learning"/"python"/"new_for_exercices"/"dictionnaire.py"

disk_d_parcours.touch()

print("Succèss")
