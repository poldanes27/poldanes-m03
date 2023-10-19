"""
Exercici 12
Implementa un programa que demani per teclat dos punts del pla i tot seguit calculi i mostri la distància entre ells.

Notes:

Un punt del pla es representa amb un parell de números. Per exemple, el punt A es representarà pels números x1 i y1, i el punt B pels números x2 i y2
La fórmula de la distància entre dos punts A i B és:

distància(A,B) = √( (x2 - x1)2 + (y2 - y1)2)
"""

# Solicita al usuario las coordenadas de los dos puntos del plano
x1 = float(input("Introduce la coordenada x del primer punto: "))
y1 = float(input("Introduce la coordenada y del primer punto: "))
x2 = float(input("Introduce la coordenada x del segundo punto: "))
y2 = float(input("Introduce la coordenada y del segundo punto: "))

# Calcula la distancia entre los dos puntos
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Muestra la distancia calculada
print("La distancia entre los puntos ({}, {}) y ({}, {}) es: {:.2f}".format(x1, y1, x2, y2, distancia))