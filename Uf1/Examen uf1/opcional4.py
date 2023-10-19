'''
Alejo Liébana
Pol Danés
ASIXBc1
11-10-2023


EOP 4
Com demanaríeu més d'una variable d'entrada en una sola línia?
'''

entrada = input("Ingresa 4 valores separados por espacios: ")

#El delimitador será un espacio pero podría ser otra cosa por ejemplo .split(":")
valor = entrada.split()

valor1 = valor[0]
valor2 = valor[1]
valor3 = valor[2]
valor4 = valor[3]

print(valor)
print(valor1)
print(valor2)
print(valor3)
print(valor4)