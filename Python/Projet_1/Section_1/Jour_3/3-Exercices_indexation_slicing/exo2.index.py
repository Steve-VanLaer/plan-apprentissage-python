mot_1 = input('Introduisez un mot qui commence par Py : ')
if mot_1[0:2] == 'Py':  # Est-ce que le mot analysé commence par les lettres 'Py' ?
    print('Le mot introdit (',mot_1,') commence bien par Py.')
else:
    print('Le mot introduit (',mot_1,') ne commence pas par Py.')
    mot_2 = input('Inroduisez un mot qui commence par Py : ')
    if mot_2[0:2] == 'Py':
        print('Bravo, vous avez trouvé un mot qui commence par Py.')
    else:
        print('Dommage, vous n\'avez pas réussi à trouver un mot qui commence par Py. Pythagore ou Python sont des mots qui commencent par Py')