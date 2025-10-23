# Faire apparaître les décimales d'une valeur float dans une concaténation
cours = float(input("Entrez le cours de l'EUR/USD avec 5 décimales : ")) 
print("Le cours de l'EUR/USD est "+cours:.2f)       # à corriger

# Faire apparaître les décimales d'une valeur float dans une chaîne de textes
print("Le cours de l'EUR/USD est ",f"{cours:.5f}")

# Faire apparaître les décimales d'une valeur float dans un format
print(f"Le cours de l'EUR/UDS est {cours:.5f}")