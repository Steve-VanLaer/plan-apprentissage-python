# Affichesr True si le nombre introduit par l'utilisateur est supérieur à 10 et pair, sinon False
nbre = int(input('Introduisez un nombre : '))
if nbre % 2 == 0 and nbre > 10:
    print(True)
else:
    print(False)