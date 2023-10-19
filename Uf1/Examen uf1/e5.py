'''
Alejo Liébana
Pol Danés
ASIXBc1
11-10-2023

E5. Encript12345
Demana una paraula per teclat i mostrar-la per pantalla, canviar les vocals per als
numèrics 1, 2, 3, 4 o 5.
Tenint en compte, que la lletra a i A és l'1, consecutivament fins a la lletra u i U que
és el 5.

'''


try:
    palabra = input("Inserta una palabra y te encripto las vocales: ")
    print(f"Tu palabra es: {palabra}")
    print("Encriptando...")

    palabra = palabra.replace("a","1")
    palabra = palabra.replace("A", "1")
    palabra = palabra.replace("e", "2")
    palabra = palabra.replace("E", "2")
    palabra = palabra.replace("i", "3")
    palabra = palabra.replace("I", "3")
    palabra = palabra.replace("o", "4")
    palabra = palabra.replace("O", "4")
    palabra = palabra.replace("u", "5")
    palabra = palabra.replace("U", "5")

    print(palabra)

except:
    print("ERROR: valor incorrecto.")