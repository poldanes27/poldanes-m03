"""
Escriu el programa que demani a l'usuari el valor de dues variables variableA i variableB .Ha d’intercanviar els seus valors. És a dir, el contingut de la variableA ha d’estar en la variableB, i el de la variableB a la variableA. Finalment els ha de mostrar per pantalla
"""
# Solicita al usuario los valores de las dos variables
variableA = input("Introduce el valor de variableA: ")
variableB = input("Introduce el valor de variableB: ")

# Intercambia los valores de las dos variables
temp = variableA
variableA = variableB
variableB = temp

# Muestra los valores intercambiados
print("Después del intercambio:")
print("Valor de variableA: " + variableA)
print("Valor de variableB: " + variableB)
