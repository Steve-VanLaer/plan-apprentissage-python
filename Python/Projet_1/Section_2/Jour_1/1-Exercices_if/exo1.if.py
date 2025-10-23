# Demander un nombre à l'utilisateur et afficher s'il est positif, négatif ou nul
nbre = int(input("Introduisez un nombre entier : "))
if nbre > 0:
    print(f"Le nombre introduit ({nbre}) est positif.")
elif nbre < 0:
    print(f"Le nombre introduit ({nbre}) est négatif.")
else:
    print(f"Le nombre introduit ({nbre}) est nul.")