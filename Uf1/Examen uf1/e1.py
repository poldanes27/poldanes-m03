'''
Alejo Liébana
Pol Danés
ASIXBc1
11-10-2023

E1. HowBigIsMyPizza
Demanar el diàmetre d'una pizza rodona i imprimeix la seva superfície.
Pots usar Math.PI per escriure el valor de Pi.

'''

import math

try:
    diametro = int(input("Qué diámetro tiene la pizza? "))
    radio = diametro / 2

    resultado = (radio * radio) * math.pi

    print(f"La superficie es: {resultado}cm")

except:
    print("ERROR: introduce un valor válido")

