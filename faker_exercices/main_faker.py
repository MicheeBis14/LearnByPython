# from faker import Faker

# fake = Faker(locale="fr_FR")
# print(fake.address())


from pathlib import Path

voie_main = Path.cwd()/"exercices_fonctions"/"main_exer10.py"
voie_main.touch(exist_ok=True)

if voie_main:
    print(voie_main)
else:
    print('eRREUR')