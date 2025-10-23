# Formater plusieurs variables
nom     = input("Introduisez votre nom : ")
prénom  = input("Introduisez votre prénom : ")
print(f"Bonjour {prénom} {nom}")

# Dans un formatage de textes les données qui ne sont pas de type string ne doivent pas être converties en string
âge = int(input("Introduisez votre âge : "))
print(f"Vous avez {âge} ans.")