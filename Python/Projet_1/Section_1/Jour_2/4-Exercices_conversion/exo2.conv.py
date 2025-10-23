# Convertir la donnée introduite en type float
print("Nous allons calculer le montant TVA de votre facture.")
htva = float(input("Introduisez le montant HTVA : "))
taux = float(input("Renseignez le taux de TVA applicable en un nombre entier : "))
tva  = htva * taux/100
print(f"Le montant TVA est de {tva:.2f} euros ")   # la partie « :.2f » permet de choisir le nombre de déimales affichées