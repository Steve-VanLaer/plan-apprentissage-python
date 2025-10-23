nombre = int(input('Introduisez un nombre en secondes : '))
minutes = nombre // 60
secondes = nombre % 60
print(f'Le nombre introduit en secondes équivaut à {minutes} minutes et {secondes} secondes.')