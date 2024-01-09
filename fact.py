print(' Dan print \n Grande imprimérie de kinshasa ')
print(' Facture proforma')
print('\n')

nom_client = input(" Veuillez saisir le nom complet du client : ").title()
print( nom_client)

detail_cli = "Saisie des informations de la facture du client {client}".format(client = nom_client)

print(detail_cli)

libelle1, size1, prix_unit1, quantite1 = input("Entrez le premier libellé svp ! : "), input("Entrez le size : "), input("Entrez le prix unitaire : "), input("Entrez la quantité : ")

libelle2, size2, prix_unit2, quantite2 = input("Entrez le deuxième libellé svp ! : "), input("Entrez le size : "), input("Entrez le prix unitaire : "), input("Entrez la quantité : ")

prix_global1 = int(prix_unit1) * int(quantite1)
prix_global2 = int(prix_unit2) * int(quantite2)

# Conversion des prix globaux afin d'appliquer la methode zfill
prixglo1 = str(prix_global1).zfill(5)
prixglo2 = str(prix_global2).zfill(5)

#  Conversion D'autres infos pour appliquer zfill
qte1 = quantite1.zfill(5)
price1 = prix_unit1.zfill(5)

qte2 = quantite2.zfill(5)
price2 = quantite2.zfill(5)

print('\n')

# PROFORMA
print   (" Libelle ", " Size ", " Prix Unitaire ", " Quantité ", " Prix Global ")
print   (      libelle1 ,          size1 ,             price1 +"CDF" ,            qte1 ,              prixglo1 )
print   (      libelle2 ,          size2 ,             price2 + "" ,            qte2 ,              prixglo2 )

