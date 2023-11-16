"""
Pol Danes
"""

valores = input("")
valores = valores.split()
personas = int(valores[0])
galletas = int(valores[1])

if personas <= galletas:
    print ("Lets Eat")
else:
    print ("Lets fight")
