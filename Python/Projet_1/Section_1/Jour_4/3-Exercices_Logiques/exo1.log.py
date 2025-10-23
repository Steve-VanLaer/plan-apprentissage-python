annee = int(input('Introduisez une année : '))
if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0 :
    print('L\année introduite est bissextile')
else:
    print('L\'année introduite n\' est pas bissextile')