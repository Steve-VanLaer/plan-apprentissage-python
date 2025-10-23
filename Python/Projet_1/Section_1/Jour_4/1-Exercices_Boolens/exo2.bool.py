# Afficher True si un mot commence par 'A'
mot = input('Introduisez un mot : ')
if mot[0:1] == 'A':
    print(True)
else:
    print(False)

# Autre option pour trouver la première lettre d'un mot
sl = slice(0,1)
if sl == 'A':
    print(True)
else:
    print(False)