mot = input('Introduisez un mot qui commence par Py : ')
if mot[0:2] == 'Py':
    print('Bravo, vous avez introdit un mot (',mot,') qui commence par Py.')
else:
    print('Le mot introduit (',mot,') ne commence pas par Py')
    mot = input('Essayez à nouveau ! Introduisez un mot qui commence par Py : ')
    if mot[0:2] == 'Py':
        print('Bravo, vous avez introduit un mot (',mot,') qui commence par Py')
    else:
        print('Dommage, vous n\'avez pas trouvé un mot qui commence par Py. Python et Pythagore sont des mots qui commencent par Py')    