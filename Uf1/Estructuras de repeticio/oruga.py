CAP= "   \...../"
ULLS= "    ╚⊙ ⊙╝"
COS = "  ╚═(███)═╝"
CUA =  "     ═V═ "

mida = int(input("Quina es la mida de la oruga: "))
print(CAP)
print(ULLS)
contador= 1
for i in range(mida):
    print(" " * contador + COS )
    contador= contador +1
print (CUA)

