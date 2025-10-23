# True si l'âge introduit est égal ou supérieur à la longueur du prénom introduit
age     = int(input('Introduisez votre âge : '))
prenom = input('Introduisez votre prénom : ')
if age >= int(len(prenom)):
    print(True)
else:
    print(False)