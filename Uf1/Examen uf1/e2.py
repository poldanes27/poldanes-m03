'''
Alejo Liébana
Pol Danés
ASIXBc1
11-10-2023

E2.  AirVolumeCalculator
Per poder fer un estudi de la ventilació d'una aula necessitem poder calcular
la quantitat d'aire que hi cap en una habitació.
Llegeix les 3 dimensions de l'aula i mostra per pantalla quin volum té.
Cal mostrar per pantalla: “El volum de l’aula és xxx m3”

'''

try:
    longitud = int(input("Introduce la LONGITUD de la habitación en metros: "))
    ancho = int(input("Introduce el ANCHO de la habitación en metros: "))
    altura = int(input("Introduce la ALTURA de la habitación en metros: "))

    resultado = altura * ancho * longitud
    print(f"El volum de la aula es {resultado} m³")

except:
    print("ERROR: Introduce bien los valores.")