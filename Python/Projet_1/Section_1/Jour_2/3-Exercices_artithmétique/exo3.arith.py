# Calculer l'aire et le périmètre d'un cercle
r           = float(input("Entrez le rayon d'un cercle : "))
import math
périmètre   = 2 * math.pi * r
aire        = math.pi * r**2
print(f"L'aire de ce cercle est {aire:.1f} et son primètre {périmètre:.1f}")

# Autre méthode pour importer le nombre pi uniquement et pas tout le module math
from math import pi
périmètre  = 2 * pi * r
aire       = pi * r**2
print("La seconde méthode donne le même résultat : ",f"{aire:.1f}","et",f"{périmètre:.1f}")