# Concaténer du texte avec le signe +
prénom      = input('Introduisez votrevotre prénom : ')
nom         = 'Van de'
nom_complet = prénom + " "+ nom     # tjs utliser le signe + pour concaténer des variables
print(nom_complet)

# Des chaînes de textes séparées par un espace sont automatiquement concaténées
texte = 'Py' 'thon' ' ' 'est' ' ' 'génial'
print(texte)

# Application plus courante de ce qui précède
texte = ('Mon texte à exécuter est bien trop long pour tenir sur une ligne, '
         'c\'est pourquoi j\'écris la suite à la ligne dans mon fichier. Mais '
         'il apparaîtra sur une ligne lors de l\'exécution du fichier.')
print(texte)

# Attention, la dernière fonctionnalité ne s'applique pas pour concaténer des variables
nom_complet = prénom nom   # Python renvoie un msg d'erreur à l'exécution (invalid syntax)