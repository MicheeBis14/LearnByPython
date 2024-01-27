
from pathlib import Path
import json
import shutil

extension = {
    
            ".png" : "Images",
            ".jpeg" : "Images",
            ".jpg" :  "Images",
            ".gif" :  "Images",
            ".mp4" :  "Videos",
            ".mov" :  "Videos",
            ".mp3" :  "Musiques",
            ".zip" :  "Archives",
            ".txt" :  "Documents",
            ".pdf" :  "Documents",
            ".xls" :  "Documents",
            ".json" :  "File_json",
            ".html" :  "File_html",
            ".exe" :  "Program",
            
        }

way_repertoire = Path.cwd().parent.parent

repertoir_for_tri = way_repertoire/"dossier_for_tri"


# Recuperons tout ce qui se trouve dans le dossier qui contient les elements qu'on veut trier

all_files = [f for f in repertoir_for_tri.iterdir() if f.is_file()]
for f in all_files:
    dossier_replace = repertoir_for_tri/ extension.get(f.suffix, "Others")
    dossier_replace.mkdir(exist_ok=True)
    f.rename(dossier_replace / f.name)



print(repertoir_for_tri)


way_rep = Path.cwd()
dossier_create = way_rep/"creating_dos"
create_file = dossier_create/"main_file_create.py"


