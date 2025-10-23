# Afficher True si la note est >= 10 et l'assiduité bonne ou si la note est >= 18, sinon False
note        = float(input('Introduisez votre note sur 20.0 : '))
assiduite   = input('Introduisez \'oui\' si vous êtes assidu, sinon \'non\' : ')
if assiduite == 'oui' and note >= 10 or note >=18:
    print(True)
else:
    print(False)