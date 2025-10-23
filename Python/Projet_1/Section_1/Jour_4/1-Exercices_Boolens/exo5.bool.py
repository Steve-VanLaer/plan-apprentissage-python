# Afficher True si le dernier caractère d'une chaîne est '0', sinon False
nbre = int(input('Introduisez un nombre : '))
nbre_str = str(nbre)
if nbre_str[-2:-1] == '0':
    print(True)
else:
    print(False)