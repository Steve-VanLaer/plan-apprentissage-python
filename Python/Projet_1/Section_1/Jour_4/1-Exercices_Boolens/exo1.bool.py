# Afficher True si l'utilisateur est né avant 2000, sinon False
naissance = input('Introduisez l\'année de votre naissance : ')
if int(naissance) < 2000:
    print('Vous êtes né avant 2000.')
else:
    print("Vous êtes né à partir de 2000.")