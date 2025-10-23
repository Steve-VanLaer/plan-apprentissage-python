# Afficher True si trois nombres sont en ordre croissant, sinon False
n1      = int(input('Introduisez un nombre : '))
n2      = int(input('Un deuxième : '))
n3      = int(input('Un troisième : '))
if n1 < n2 and n2 < n3:
    print(True)
else:
    print(False)