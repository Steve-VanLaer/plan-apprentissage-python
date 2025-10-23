# Inverser les caractères d'une chaîne
texte   = "Bonjour"
inverse = texte[::-1]
print(inverse)

# Autre méthode
inverse = "".join(reversed(texte))
print(inverse)

# Avec une boucle
inverse = ""
for c in texte:
    inverse = c + inverse
print(inverse)