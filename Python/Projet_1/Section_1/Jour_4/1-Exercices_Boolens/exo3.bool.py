# concaténer une chaîne, compter ses caractères et afficher True si >= 10, sinon False
prénom  = input('Introduisez votre prénom : ')
nom     = input('Introduisez votre nom : ')
nom_complet = prénom + nom
if len(nom_complet) >=10:
    print(True)
else:
    print(not True)
