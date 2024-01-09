ann = int(input('Veuillez entrer une année svp ! :'))

if ann % 400 == 0 or ann % 4 == 0 and ann % 100 != 0 :
    print("L'année " + str(ann) + " que vous avez saisi est une année bissextile" )
else:
    print("L'année " + str(ann) + " que vous avez saisi n'est pas une année bissextile" )

    