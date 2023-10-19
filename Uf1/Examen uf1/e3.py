'''
Alejo Liébana
Pol Danés
ASIXBc1
11-10-2023

E3. InRange
Escriu un programa que llegeixi 5 enters. El primer i el segon creen un rang,
el tercer i el quart creen un altre rang. Mostra True si el cinquè valor,
està comprès dins els dos rangs, si no False. (Els extrems dels rangs inclosos)

'''

try:
    n1 = int(input("Inserta el 1 número: "))
    n2 = int(input("Inserta el 2 número: "))

    n3 = int(input("Inserta el 3 número: "))
    n4 = int(input("Inserta el 4 número: "))

    n5 = int(input("Inserta el 5 número y comprobaremos si está en los dos rangos a la vez: "))

    print(n5 >= n1 and n5 <= n2 and n5 >= n3 and n5 <= n4)

    #Otra manera con 2 salidas que dan más información

    #if n5 >= n1 and n5 <= n2 and n5 >= n3 and n5 <= n4:
    #    print("TRUE: Está en los 2 rangos a la vez")
    #else:
    #    print("FALSE: No está en los 2 rangos a la vez")

except:
    print("ERROR: escribe un número.")