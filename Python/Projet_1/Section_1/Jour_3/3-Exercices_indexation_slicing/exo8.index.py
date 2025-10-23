# Slicer une chaîne de caractères en deux
chaine = "Python"
sl     = slice(0,3)     # slicer de l'index 0 jusqu'à 2 exclu
print(chaine[sl])       # appliquer le slice

# Autre méthode
sl     = chaine[0:3]
print(sl)

# Appliquer un slice avec unpas 
mot = 'programmation'
sl  = slice(0,8,2)      # slicer de l'index 0 ('p') jusqu'à l'index 8 exclu ('a') avec un pas de deux (p,o,r,m)
print(mot[sl])