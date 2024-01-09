my_key = "bkmichee2023"

nom = input("Veuillez saisir votre nom svp ! : ").title()
print('\n')

mot_de_pass = input("Veuillez entrer votre mot de passe svp !")

print('\n')

if mot_de_pass == my_key:
    salutation = f"Bienvenu sur notre portail {nom}"
    print('\n')
    print(salutation)
else:
    desole = f"Desolé Monsieur ou Madame {nom} il y a erreur de mot de pass, prière de réessayer plus tard"
    print(desole)
