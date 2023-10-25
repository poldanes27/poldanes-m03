"""
HowManyDaysInMonth - Pol Danes

"""
mes = int(input("Digues un mes en numero: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 11:
    print("31 dies")

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("30 dies")

elif mes == 2:
    print("te 29 o 28 dies")

else:
    print("Eres tonto")
"""
numero = input("")
match numero:
    case "1" | "3" | "5" | "7" | "8" | "10" | "11" |:print ("31")
    case "4 "| "6" | "9" | "11":print("30")
    case "2": print("28")
    case _: print ("Mes no valid")
"""