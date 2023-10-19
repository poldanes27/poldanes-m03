"""
Exercici 18
Escriu un programa que donat el nom i els dos cognoms introduïts per un usuari, mostri, només, les inicials corresponents en majúscules.
"""
nom = input("Introdueix el teu nom: ")
cognom1 = input("Introdueix el teu primer cognom: ")
cognom2 = input("Introdueix el teu segon cognom: ")

# Obté les inicials en majúscules i la comanda upper serveix per convertir las minusculas en mayusculas
inicial_nom = nom[0].upper()
inicial_cognom1 = cognom1[0].upper()
inicial_cognom2 = cognom2[0].upper()

# Mostra les inicials
print("Les inicials del teu nom i cognoms són:", inicial_nom, inicial_cognom1, inicial_cognom2)
