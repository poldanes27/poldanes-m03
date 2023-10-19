#Pol Danes#

doseuros = int(input("Quantas monedas tienes de 2 euros: "))
uneuro = int(input("Quantas monedas tienes de 1 euro: "))
cincuantacentims = int(input("Quantas monedas tienes de 50 centimos: "))
vintsentims = int(input("Quantas monedas tienes de 20 centimos: "))
deusentims = int(input("Quantas monedas tienes de 10 centimos: "))
cincsentims = int(input("Quantas monedas tienes de 5 centimos: "))

resultado2 = doseuros*2
resultado50 = cincuantacentims / 2
resultado20 = vintsentims *0.20
resultado10 = deusentims *0.10
resultado5 = cincsentims *0.05

resultado = float(resultado5 +resultado10 + resultado20 + resultado50 + resultado2,)
print ("Tens: ", resultado)