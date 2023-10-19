'''
Alejo Liébana
Pol Danés
ASIXBc1
11-10-2023

E4. WorkingAge
Escriu un programa que llegeixi l'edat de l'usuari i mostri si té edat per treballar,
 l'edat mínima per treballar legalment és 16 i suposarem l'edat màxima als 65.

Consultar: Python If Statement. La sentència if es veurà a més detalls en el proper tema.

'''

try:
    edad = int(input("Inserta tu edad y te digo si puedes trabajar: "))
    if edad >= 16 and edad <= 65:
        print("Puedes currar.")
    else:
        print("NO puedes trabajar.")


except:
    print("ERROR: Inserta un número.")
