# Calculer le prix TVAC à partir du prix HTVA et TVA, renseignés par l'utilisateur
htva = float(input("Introduisez le montant HTVA : "))
tva  = float(input("Introduisez le montant TVA : "))
tvac = htva + tva
print("Le montant TVAC est ",f"{tvac:.2f}")