# Demander un nombre entier à l'utilisateur et afficher s'il est pair ou impair
nbre = int(input("Introduisez un nombre entier : "))
if nbre % 2 == 0:
    print(f"Le nombre introduit ({nbre}) est pair.")
else:
    print(f"Le nombre introduit ({nbre}) est impair.")