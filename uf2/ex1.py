"""
PolDanes
"""
equip1 = input("")
equip2 = input("")

def analitzar_resultat(puntuacio):
    if puntuacio[0] == 0 and puntuacio[1] == 2:
        print("Cistella de " + equip2)
    elif puntuacio[0] == 0 and puntuacio[1] == 5:
        print("Triple de " + equip2)
    elif puntuacio[0] == 2 and puntuacio[1] == 5:
        print("Cistella de " + equip1)
    elif puntuacio[0] == 3 and puntuacio[1] == 5:
        print("Tir lliure de " + equip1)


resultats_partit = []
while True:
    resultat = input("Introdueix el resultat actual (o -1 per acabar): ")
    if resultat == "-1":
        break
    else:
        resultats_partit.append(tuple(map(int, resultat.split())))
for resultat in resultats_partit:
    analitzar_resultat(resultat)
if resultats_partit[-1][0] > resultats_partit[-1][1]:
    print("Guanya " + equip1)
else:
    print("Guanya " + equip2)
